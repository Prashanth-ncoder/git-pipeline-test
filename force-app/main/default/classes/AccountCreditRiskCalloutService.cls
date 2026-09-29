//test
public with sharing class AccountCreditRiskCalloutService implements Queueable, Database.AllowsCallouts {
    //test

    private Id accountId;

    public AccountCreditRiskCalloutService(Id accountId) {
        this.accountId = accountId;
    }

    public static void processHighValueOpportunity(Opportunity opp) {
        String existingOppDescription = String.isBlank(opp.Description) ? '' : opp.Description;
        opp.Description = '[CREDIT_CHECK_QUEUED] ' + existingOppDescription;
        update opp;

        enqueueCreditCheck(opp.AccountId);
    }

    public static void enqueueCreditCheck(Id accountId) {
        System.enqueueJob(new AccountCreditRiskCalloutService(accountId));
    }

    public void execute(QueueableContext context) {
        Account acc = [SELECT Id, Name, Description FROM Account WHERE Id = :accountId];

        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:CreditRiskAPI/check?accountId=' + accountId);
        req.setMethod('GET');
        req.setTimeout(10000);

        Http http = new Http();

        try {
            HttpResponse res = http.send(req);

            if (res.getStatusCode() == 200) {
                Map<String, Object> body = (Map<String, Object>) JSON.deserializeUntyped(res.getBody());
                String riskLevel = (String) body.get('riskLevel');

                String existingDescription = String.isBlank(acc.Description) ? '' : acc.Description;
                acc.Description = '[CREDIT_RISK: ' + riskLevel + '] ' + existingDescription;
                update acc;
            } else {
                logFailure(acc, 'Credit API returned status ' + res.getStatusCode());
            }
        } catch (Exception e) {
            logFailure(acc, 'Credit API callout failed: ' + e.getMessage());
        }
    }

    private static void logFailure(Account acc, String reason) {
        String existingDescription = String.isBlank(acc.Description) ? '' : acc.Description;
        acc.Description = '[CREDIT_CHECK_FAILED] ' + existingDescription;
        update acc;
        System.debug(LoggingLevel.ERROR, reason);
    }
}
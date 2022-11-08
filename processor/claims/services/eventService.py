
# An async method that doesn't block the processing
async def sendClaimProcessedEvent(claims_data):
    # Send an event to payments queue
    # On success send
    # On failure, send the events to a failure queue
    # We can then setup a cron job that shovels all messages from failure queue back into main queue
    # Upon multiple failures, create an alert to the person on call to troubleshoot what's causing the error
    # Alerts can be made using PagerDuty or any other platform
    # Metrics can be captured using Datadog, Newrelic etc
    return True


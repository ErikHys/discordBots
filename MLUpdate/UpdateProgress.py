from discord import Webhook, RequestsWebhookAdapter


def send_update(info):
    webhook = Webhook.from_url("https://discord.com/api/webhooks/909411094005678080/"
                               "YiAaNsxElY9bpGI72Y2mHMNOjebuy_5ird08iuZnCw8mKZzQUkiLeA5jQkJHmPSo3oVs",
                               adapter=RequestsWebhookAdapter())
    webhook.send("New update: " + info)
    print("done")

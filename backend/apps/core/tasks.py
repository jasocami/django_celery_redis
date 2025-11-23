from celery import shared_task


@shared_task
def add(x,y):
    result = x + y

    from django.core.mail import send_mail

    send_mail( "Result task",
        f"Result is {result}",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )

    return result

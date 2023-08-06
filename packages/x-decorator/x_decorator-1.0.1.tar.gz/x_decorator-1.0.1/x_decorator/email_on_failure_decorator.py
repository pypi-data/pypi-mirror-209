# import smtplib
# import traceback

# from email.mime.text import MIMEText


# def email_on_failure(sender_email, password, recipient_email):
#     """
#         a very useful decorator in production systems is the notification decorator.
#         Once again, even with several retries,
#         even a well-tested codebase fails. And when that happens,
#          we need to inform someone about it to take quick action.


#          EX:
#          @email_on_failure(sender_email='your_email@gmail.com', password='your_password',
#                   recipient_email='recipient_email@gmail.com')
#         def my_function():
#             # code that might fail
#             pass
#     """

#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 # format the error message and traceback
#                 err_msg = f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"

#                 # create the email message
#                 message = MIMEText(err_msg)
#                 message['Subject'] = f"{func.__name__} failed"
#                 message['From'] = sender_email
#                 message['To'] = recipient_email

#                 # send the email
#                 with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#                     smtp.login(sender_email, password)
#                     smtp.sendmail(sender_email, recipient_email, message.as_string())

#                 # re-raise the exception
#                 raise

#         return wrapper

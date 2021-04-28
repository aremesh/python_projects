from plyer import notification
from parser import parser

args = parser.parse_args()

title = args.title
message = args.message

notification.notify(
    title=title,  # Title of the notification
    message=message,  # Message of the notification
    app_icon= None,  # Icon to be displayed along with the message 
    # app_name = "Desktop notifier",  # Name of the app launching this notification
    timeout = 2,  # Time to display the message for, defaults to 10
    toast = False)  # Simple message instead of full notification

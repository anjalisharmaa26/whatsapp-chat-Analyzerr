# import re
# import pandas as pd
#
# def preprocess(data):
#     try:
#         try:
#             pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:am|pm)?\s*-\s'
#
#             messages = re.split(pattern, data)[1:]
#
#             dates = re.findall(pattern, data)
#
#             df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#             df['message_date'] = pd.to_datetime(df['message_date'].str.replace('\u202F', ' '),
#                                                 format='%d/%m/%y, %I:%M %p -')
#
#             users = []
#             messages = []
#             for message in df['user_message']:
#                 entry = re.split('([\w\W]+?):\s', message)
#                 if entry[1:]:  # user name
#                     users.append(entry[1])
#                     messages.append(" ".join(entry[2:]))
#                 else:
#                     users.append('group_notification')
#                     messages.append(entry[0])
#
#             df['user'] = users
#             df['message'] = messages
#             df.drop(columns=['user_message'], inplace=True)
#
#             df.rename(columns={'message_date': 'date'}, inplace=True)
#             df['only_date'] = df['date'].dt.date
#             df['year'] = df['date'].dt.year
#             df['month_num'] = df['date'].dt.month
#             df['month'] = df['date'].dt.month_name()
#             df['day'] = df['date'].dt.day
#             df['day_name'] = df['date'].dt.day_name()
#             df['hour'] = df['date'].dt.hour
#             df['minute'] = df['date'].dt.minute
#
#             period = []
#             for hour in df[['day_name', 'hour']]['hour']:
#                 if hour == 23:
#                     period.append(str(hour) + "-" + str('00'))
#                 elif hour == 0:
#                     period.append(str('00') + "-" + str(hour + 1))
#                 else:
#                     period.append(str(hour) + "-" + str(hour + 1))
#
#             df['period'] = period
#         except:
#             try:
#                 pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*-\s'
#
#                 messages = re.split(pattern, data)[1:]
#
#                 dates = re.findall(pattern, data)
#
#                 df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#                 df['message_date'] = pd.to_datetime(df['message_date'].str.replace('\u202F', ' '),
#                                                     format='%d/%m/%y, %H:%M - ')
#                 df.rename(columns={'message_date': 'date'}, inplace=True)
#
#                 df.rename(columns={'message_date': 'date'}, inplace=True)
#
#                 users = []
#                 messages = []
#                 for message in df['user_message']:
#                     entry = re.split('([\w\W]+?):\s', message)
#                     if entry[1:]:  # user name
#                         users.append(entry[1])
#                         messages.append(" ".join(entry[2:]))
#                     else:
#                         users.append('group_notification')
#                         messages.append(entry[0])
#
#                 df['user'] = users
#                 df['message'] = messages
#                 df.drop(columns=['user_message'], inplace=True)
#
#                 df['only_date'] = df['date'].dt.date
#                 df['year'] = df['date'].dt.year
#                 df['month_num'] = df['date'].dt.month
#                 df['month'] = df['date'].dt.month_name()
#                 df['day'] = df['date'].dt.day
#                 df['day_name'] = df['date'].dt.day_name()
#                 df['hour'] = df['date'].dt.hour
#                 df['minute'] = df['date'].dt.minute
#
#                 period = []
#                 for hour in df[['day_name', 'hour']]['hour']:
#                     if hour == 23:
#                         period.append(str(hour) + "-" + str('00'))
#                     elif hour == 0:
#                         period.append(str('00') + "-" + str(hour + 1))
#                     else:
#                         period.append(str(hour) + "-" + str(hour + 1))
#
#                 df['period'] = period
#             except:
#                 pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*-\s'
#
#                 messages = re.split(pattern, data)[1:]
#
#                 dates = re.findall(pattern, data)
#
#                 df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#                 df['message_date'] = pd.to_datetime(df['message_date'],
#                                                     format='%d/%m/%Y, %H:%M - ')
#                 df.rename(columns={'message_date': 'date'}, inplace=True)
#
#                 df.rename(columns={'message_date': 'date'}, inplace=True)
#
#                 users = []
#                 messages = []
#                 for message in df['user_message']:
#                     entry = re.split(r'([\w\W]+?):\s', message)
#                     if entry[1:]:  # user name
#                         users.append(entry[1])
#                         messages.append(" ".join(entry[2:]))
#                     else:
#                         users.append('group_notification')
#                         messages.append(entry[0])
#
#                 df['user'] = users
#                 df['message'] = messages
#                 df.drop(columns=['user_message'], inplace=True)
#
#                 df['only_date'] = df['date'].dt.date
#                 df['year'] = df['date'].dt.year
#                 df['month_num'] = df['date'].dt.month
#                 df['month'] = df['date'].dt.month_name()
#                 df['day'] = df['date'].dt.day
#                 df['day_name'] = df['date'].dt.day_name()
#                 df['hour'] = df['date'].dt.hour
#                 df['minute'] = df['date'].dt.minute
#
#                 period = []
#                 for hour in df[['day_name', 'hour']]['hour']:
#                     if hour == 23:
#                         period.append(str(hour) + "-" + str('00'))
#                     elif hour == 0:
#                         period.append(str('00') + "-" + str(hour + 1))
#                     else:
#                         period.append(str(hour) + "-" + str(hour + 1))
#
#                 df['period'] = period
#     except:
#         try:
#             pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:am|pm)?\s*-\s'
#
#             messages = re.split(pattern, data)[1:]
#
#             dates = re.findall(pattern, data)
#
#             df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#             df['message_date'] = pd.to_datetime(df['message_date'].str.replace('\u202F', ' '),
#                                                 format='%d/%m/%y, %I:%M %p - ')
#             df.rename(columns={'message_date': 'date'}, inplace=True)
#
#             df.rename(columns={'message_date': 'date'}, inplace=True)
#
#             users = []
#             messages = []
#             for message in df['user_message']:
#                 entry = re.split('([\w\W]+?):\s', message)
#                 if entry[1:]:  # user name
#                     users.append(entry[1])
#                     messages.append(" ".join(entry[2:]))
#                 else:
#                     users.append('group_notification')
#                     messages.append(entry[0])
#
#             df['user'] = users
#             df['message'] = messages
#             df.drop(columns=['user_message'], inplace=True)
#
#             df['only_date'] = df['date'].dt.date
#             df['year'] = df['date'].dt.year
#             df['month_num'] = df['date'].dt.month
#             df['month'] = df['date'].dt.month_name()
#             df['day'] = df['date'].dt.day
#             df['day_name'] = df['date'].dt.day_name()
#             df['hour'] = df['date'].dt.hour
#             df['minute'] = df['date'].dt.minute
#
#             period = []
#             for hour in df[['day_name', 'hour']]['hour']:
#                 if hour == 23:
#                     period.append(str(hour) + "-" + str('00'))
#                 elif hour == 0:
#                     period.append(str('00') + "-" + str(hour + 1))
#                 else:
#                     period.append(str(hour) + "-" + str(hour + 1))
#
#             df['period'] = period
#         except:
#             pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?\s*-\s'
#             messages = re.split(pattern, data)[1:]
#             dates = re.findall(pattern, data)
#             df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#             # df['message_date'] = pd.to_datetime(df['message_date'].str.replace('\u202F', ' '), format='%d/%m/%y, %I:%M %p - ')
#             # df.rename(columns = {'message_date':'date'}, inplace=True)
#             # df.head()
#             df['message_date'] = pd.to_datetime(
#                 df['message_date'].str.replace('\u202F', ' ').str.rstrip(' -'),  # Remove special space & trailing " -"
#                 format='%m/%d/%y, %I:%M %p',  # Correct format
#                 errors='coerce'  # Handle unexpected values safely
#             )
#
#             df.rename(columns={'message_date': 'date'}, inplace=True)
#
#             users = []
#             messages = []
#             for message in df['user_message']:
#                 entry = re.split('([\w\W]+?):\s', message)
#                 if entry[1:]:  # user name
#                     users.append(entry[1])
#                     messages.append(" ".join(entry[2:]))
#                 else:
#                     users.append('group_notification')
#                     messages.append(entry[0])
#
#             df['user'] = users
#             df['message'] = messages
#             df.drop(columns=['user_message'], inplace=True)
#
#             df['only_date'] = df['date'].dt.date
#             df['year'] = df['date'].dt.year
#             df['month_num'] = df['date'].dt.month
#             df['month'] = df['date'].dt.month_name()
#             df['day'] = df['date'].dt.day
#             df['day_name'] = df['date'].dt.day_name()
#             df['hour'] = df['date'].dt.hour
#             df['minute'] = df['date'].dt.minute
#
#             period = []
#             for hour in df[['day_name', 'hour']]['hour']:
#                 if hour == 23:
#                     period.append(str(hour) + "-" + str('00'))
#                 elif hour == 0:
#                     period.append(str('00') + "-" + str(hour + 1))
#                 else:
#                     period.append(str(hour) + "-" + str(hour + 1))
#
#             df['period'] = period
#
#
#
#     # try:
#     #     try:
#
#     #     except:
#     #         pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:am|pm)?\s*-\s'
#     #
#     #         messages = re.split(pattern, data)[1:]
#     #
#     #         dates = re.findall(pattern, data)
#     #
#     #         df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#     #         df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
#     #         # if df['message_date'] is None:
#     #         #     df['message_date'] = pd.to_datetime(
#     #         #         df['message_date'].str.replace('\u202F', ' ').str.rstrip(' -'),
#     #         #         # Remove special space & trailing " -"
#     #         #         format='%m/%d/%y, %I:%M %p',  # Correct format
#     #         #         errors='coerce'  # Handle unexpected values safely
#     #         #     )
#     #
#     #
#     #         users = []
#     #         messages = []
#     #         for message in df['user_message']:
#     #             entry = re.split('([\w\W]+?):\s', message)
#     #             if entry[1:]:  # user name
#     #                 users.append(entry[1])
#     #                 messages.append(" ".join(entry[2:]))
#     #             else:
#     #                 users.append('group_notification')
#     #                 messages.append(entry[0])
#     #
#     #         df['user'] = users
#     #         df['message'] = messages
#     #         df.drop(columns=['user_message'], inplace=True)
#     #
#     #         df.rename(columns={'message_date': 'date'}, inplace=True)
#     #
#     #         df['only_date'] = df['date'].dt.date
#     #         df['year'] = df['date'].dt.year
#     #         df['month_num'] = df['date'].dt.month
#     #         df['month'] = df['date'].dt.month_name()
#     #         df['day'] = df['date'].dt.day
#     #         df['day_name'] = df['date'].dt.day_name()
#     #         df['hour'] = df['date'].dt.hour
#     #         df['minute'] = df['date'].dt.minute
#     #
#     #         period = []
#     #         for hour in df[['day_name', 'hour']]['hour']:
#     #             if hour == 23:
#     #                 period.append(str(hour) + "-" + str('00'))
#     #             elif hour == 0:
#     #                 period.append(str('00') + "-" + str(hour + 1))
#     #             else:
#     #                 period.append(str(hour) + "-" + str(hour + 1))
#     #
#     #         df['period'] = period
#     # except:
#     #     try:
#
#     #     except:
#     #         try:
#     #             pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:AM|PM)?\s*-\s'
#     #
#     #             messages = re.split(pattern, data)[1:]
#     #
#     #             dates = re.findall(pattern, data)
#     #
#     #             df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#     #             df['message_date'] = pd.to_datetime(df['message_date'].str.replace('\u202F', ' '),
#     #                                                 format='%d/%m/%y, %I:%M %p - ')
#     #             df.rename(columns={'message_date': 'date'}, inplace=True)
#     #
#     #             df.rename(columns={'message_date': 'date'}, inplace=True)
#     #
#     #             users = []
#     #             messages = []
#     #             for message in df['user_message']:
#     #                 entry = re.split('([\w\W]+?):\s', message)
#     #                 if entry[1:]:  # user name
#     #                     users.append(entry[1])
#     #                     messages.append(" ".join(entry[2:]))
#     #                 else:
#     #                     users.append('group_notification')
#     #                     messages.append(entry[0])
#     #
#     #             df['user'] = users
#     #             df['message'] = messages
#     #             df.drop(columns=['user_message'], inplace=True)
#     #
#     #             df['only_date'] = df['date'].dt.date
#     #             df['year'] = df['date'].dt.year
#     #             df['month_num'] = df['date'].dt.month
#     #             df['month'] = df['date'].dt.month_name()
#     #             df['day'] = df['date'].dt.day
#     #             df['day_name'] = df['date'].dt.day_name()
#     #             df['hour'] = df['date'].dt.hour
#     #             df['minute'] = df['date'].dt.minute
#     #
#     #             period = []
#     #             for hour in df[['day_name', 'hour']]['hour']:
#     #                 if hour == 23:
#     #                     period.append(str(hour) + "-" + str('00'))
#     #                 elif hour == 0:
#     #                     period.append(str('00') + "-" + str(hour + 1))
#     #                 else:
#     #                     period.append(str(hour) + "-" + str(hour + 1))
#     #
#     #             df['period'] = period
#     #
#     #         except:
#     #             try:
#     #                 pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:AM|PM)?\s*-\s'
#     #
#     #                 messages = re.split(pattern, data)[1:]
#     #
#     #                 dates = re.findall(pattern, data)
#     #
#     #                 df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#     #                 df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p- ')
#     #                 df.rename(columns={'message_date': 'date'}, inplace=True)
#     #
#     #                 df.rename(columns={'message_date': 'date'}, inplace=True)
#     #
#     #                 users = []
#     #                 messages = []
#     #                 for message in df['user_message']:
#     #                     entry = re.split('([\w\W]+?):\s', message)
#     #                     if entry[1:]:  # user name
#     #                         users.append(entry[1])
#     #                         messages.append(" ".join(entry[2:]))
#     #                     else:
#     #                         users.append('group_notification')
#     #                         messages.append(entry[0])
#     #
#     #                 df['user'] = users
#     #                 df['message'] = messages
#     #                 df.drop(columns=['user_message'], inplace=True)
#     #
#     #                 df['only_date'] = df['date'].dt.date
#     #                 df['year'] = df['date'].dt.year
#     #                 df['month_num'] = df['date'].dt.month
#     #                 df['month'] = df['date'].dt.month_name()
#     #                 df['day'] = df['date'].dt.day
#     #                 df['day_name'] = df['date'].dt.day_name()
#     #                 df['hour'] = df['date'].dt.hour
#     #                 df['minute'] = df['date'].dt.minute
#     #
#     #                 period = []
#     #                 for hour in df[['day_name', 'hour']]['hour']:
#     #                     if hour == 23:
#     #                         period.append(str(hour) + "-" + str('00'))
#     #                     elif hour == 0:
#     #                         period.append(str('00') + "-" + str(hour + 1))
#     #                     else:
#     #                         period.append(str(hour) + "-" + str(hour + 1))
#     #
#     #                 df['period'] = period
#     #             except:
#     #                 pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:AM|PM)?\s*-\s'
#     #
#     #                 messages = re.split(pattern, data)[1:]
#     #
#     #                 dates = re.findall(pattern, data)
#     #
#     #                 df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#     #                 df['message_date'] = pd.to_datetime(
#     #                     df['message_date'].str.replace('\u202F', ' ').str.rstrip(' -'),
#     #                     # Remove special space & trailing " -"
#     #                     format='%m/%d/%y, %I:%M %p',  # Correct format
#     #                     errors='coerce'  # Handle unexpected values safely
#     #                 )
#     #
#     #                 users = []
#     #                 messages = []
#     #                 for message in df['user_message']:
#     #                     entry = re.split('([\w\W]+?):\s', message)
#     #                     if entry[1:]:  # user name
#     #                         users.append(entry[1])
#     #                         messages.append(" ".join(entry[2:]))
#     #                     else:
#     #                         users.append('group_notification')
#     #                         messages.append(entry[0])
#     #
#     #
#     #                 df['user'] = users
#     #                 df['message'] = messages
#     #                 df.drop(columns=['user_message'], inplace=True)
#     #
#     #                 df.rename(columns={'message_date': 'date'}, inplace=True)
#     #                 df['only_date'] = df['date'].dt.date
#     #                 df['year'] = df['date'].dt.year
#     #                 df['month_num'] = df['date'].dt.month
#     #                 df['month'] = df['date'].dt.month_name()
#     #                 df['day'] = df['date'].dt.day
#     #                 df['day_name'] = df['date'].dt.day_name()
#     #                 df['hour'] = df['date'].dt.hour
#     #                 df['minute'] = df['date'].dt.minute
#     #
#     #                 period = []
#     #                 for hour in df[['day_name', 'hour']]['hour']:
#     #                     if hour == 23:
#     #                         period.append(str(hour) + "-" + str('00'))
#     #                     elif hour == 0:
#     #                         period.append(str('00') + "-" + str(hour + 1))
#     #                     else:
#     #                         period.append(str(hour) + "-" + str(hour + 1))
#     #
#     #                 df['period'] = period
#     #                 # return "Hello"
#
#     return df
import re
import pandas as pd

def preprocess(data):
    try:
        # Remove system messages (end-to-end encryption messages)
        data = re.sub(r'.*Messages and calls are end-to-end encrypted.*\n', '', data)

        # Regex pattern for timestamps (handles multiple formats)
        pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?\s*-\s'

        # Extract messages and timestamps
        messages = re.split(pattern, data)[1:]
        dates = re.findall(pattern, data)

        # Create DataFrame
        df = pd.DataFrame({'user_message': messages, 'message_date': dates})

        # Standardize date format (remove special spaces & trailing "-")
        df['message_date'] = df['message_date'].str.replace('\u202F', ' ').str.rstrip(' -')

        # Try parsing dates with multiple formats
        for fmt in ['%d/%m/%y, %I:%M %p', '%d/%m/%y, %H:%M', '%m/%d/%y, %I:%M %p', '%m/%d/%y, %H:%M',
                    '%d/%m/%Y, %I:%M %p', '%d/%m/%Y, %H:%M', '%m/%d/%Y, %I:%M %p', '%m/%d/%Y, %H:%M']:
            try:
                df['message_date'] = pd.to_datetime(df['message_date'], format=fmt)
                break
            except ValueError:
                continue

        # Rename column
        df.rename(columns={'message_date': 'date'}, inplace=True)

        # Extract users and messages
        users, messages = [], []
        for message in df['user_message']:
            entry = re.split(r'([\w\W]+?):\s', message)
            if entry[1:]:  # If a user is detected
                users.append(entry[1])
                messages.append(" ".join(entry[2:]))
            else:  # System messages
                users.append('group_notification')
                messages.append(entry[0])

        df['user'] = users
        df['message'] = messages
        df.drop(columns=['user_message'], inplace=True)

        # Remove media and deleted messages
        df = df[~df['message'].isin(['<Media omitted>', 'null', 'This message was deleted'])]

        # Extract time-based features
        df['only_date'] = df['date'].dt.date
        df['year'] = df['date'].dt.year
        df['month_num'] = df['date'].dt.month
        df['month'] = df['date'].dt.month_name()
        df['day'] = df['date'].dt.day
        df['day_name'] = df['date'].dt.day_name()
        df['hour'] = df['date'].dt.hour
        df['minute'] = df['date'].dt.minute

        # Generate time periods
        df['period'] = df['hour'].apply(lambda h: f"{h}-{'00' if h == 23 else h + 1}")

        return df

    except Exception as e:
        print("Error in preprocessing:", e)
        return None


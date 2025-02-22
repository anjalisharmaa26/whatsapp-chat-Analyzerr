# Streamlit App
import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")
st.sidebar.title("\ud83d\udcca WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("\ud83d\udcce Choose a WhatsApp Chat File")
if uploaded_file:
    data = uploaded_file.getvalue().decode("utf-8")
    df = preprocessor.preprocess(data)
    if df.empty:
        st.error("Failed to parse the chat data. Ensure it's a valid exported WhatsApp chat file.")
    else:
        df['user'] = df['user'].fillna("Unknown")
        user_list = sorted(df['user'].dropna().unique().tolist())
        if 'group_notification' in user_list:
            user_list.remove('group_notification')
        user_list.insert(0, "Overall")

        selected_user = st.sidebar.selectbox("\ud83d\udc65 Analyze messages of", user_list)
        if st.sidebar.button("\ud83d\udd0d Show Analysis"):
            num_messages, words, num_media, num_links = helper.fetch_stats(selected_user, df)
            st.markdown("## \ud83d\udcca Chat Statistics")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("💬 Total Messages", num_messages)
            col2.metric("📝 Words", words)
            col3.metric("📸 Media Shared", num_media)
            col4.metric("🔗 Links Shared", num_links)

            # Monthly Timeline
            st.markdown("## 📅 Monthly Activity Timeline")
            timeline = helper.monthly_timeline(selected_user, df)
            if not timeline.empty:
                fig = px.line(timeline, x='time', y='message', markers=True, template="plotly_dark")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data available.")

            # Daily Trends
            st.markdown("## 🗓 Daily Trends")
            daily_timeline = helper.daily_timeline(selected_user, df)
            if not daily_timeline.empty:
                fig = px.line(daily_timeline, x='only_date', y='message', markers=True, template="plotly_dark")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data available.")

            # Most Active Users
            if selected_user == 'Overall':
                st.markdown("## 🔥 Most Active Users")
                x, new_df = helper.most_busy_users(df)
                if not x.empty:
                    fig = px.bar(x.reset_index(), x='index', y=x.columns[0], color=x.columns[0], template="plotly_dark")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("No data available.")

            # Wordcloud
            st.markdown("## ☁️ WordCloud")
            df_wc = helper.create_wordcloud(selected_user, df)
            if df_wc is not None:
                fig, ax = plt.subplots()
                ax.imshow(df_wc, interpolation='bilinear')
                ax.axis("off")
                st.pyplot(fig, use_container_width=True)
            else:
                st.warning("No data available.")

            # Emoji Analysis
            st.markdown("## 😂 Emoji Analysis")
            emoji_df = helper.emoj_helper(selected_user, df)
            if not emoji_df.empty:
                fig = go.Figure(data=[go.Pie(labels=emoji_df[0], values=emoji_df[1], textinfo="label+percent")])
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data available.")

            # Weekly Activity Heatmap
            st.markdown("## 📆 Weekly Activity Heatmap")
            heatmap = helper.activity_heat_map(selected_user, df)
            if not heatmap.empty:
                fig, ax = plt.subplots()
                sns.heatmap(heatmap, cmap="mako", annot=False, linewidths=0, ax=ax)
                st.pyplot(fig)
            else:
                st.warning("No data available.")

import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# --- Streamlit Page Config ---
st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")
st.sidebar.title("📊 WhatsApp Chat Analyzer")

# --- File Upload ---
uploaded_file = st.sidebar.file_uploader("📂 Choose a WhatsApp Chat File")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("👥 Analyze messages of", user_list)

    if st.sidebar.button("🔍 Show Analysis"):

        # --- Display Key Statistics ---
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.markdown("## 📊 **Chat Statistics**")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="💬 Total Messages", value=num_messages)
        col2.metric(label="📝 Total Words", value=words)
        col3.metric(label="📸 Media Shared", value=num_media_messages)
        col4.metric(label="🔗 Links Shared", value=num_links)

        # --- Monthly Timeline ---
        st.markdown("## 📅 **Monthly Activity Timeline**")
        timeline = helper.monthly_timeline(selected_user, df)
        fig = px.line(timeline, x='time', y='message', markers=True, line_shape="spline",
                      labels={"time": "Month", "message": "Message Count"},
                      template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

        # --- Daily Timeline ---
        st.markdown("## 🗓 **Daily Message Trends**")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig = px.line(daily_timeline, x='only_date', y='message', markers=True, line_shape="spline",
                      labels={"only_date": "Date", "message": "Message Count"},
                      template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

        # --- Most Active Users (Group Level) ---
        if selected_user == 'Overall':
            st.markdown("## 🔥 **Most Active Users**")
            x, new_df = helper.most_busy_users(df)

            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(new_df.style.set_properties(**{'background-color': '#1E1E1E', 'color': 'white'}))

            with col2:
                fig = px.bar(x, x=x.index, y=x.values, labels={'x': 'Users', 'y': 'Messages'},
                             color=x.values, color_continuous_scale="reds", template="plotly_dark")
                fig.update_traces(marker=dict(line=dict(color='white', width=1)))
                fig.update_layout(xaxis_title="User", yaxis_title="Messages Sent", showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

        # --- Wordcloud ---
        st.markdown("## ☁️ **WordCloud - Most Used Words**")
        df_wc = helper.create_wordcloud(selected_user, df)

        # Convert WordCloud object to an image before displaying
        fig, ax = plt.subplots()
        ax.imshow(df_wc, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig, use_container_width=True)

        # --- Most Common Words ---
        most_common_df = helper.most_common_words(selected_user, df)
        st.markdown("## 🔠 **Most Common Words Used**")
        fig = px.bar(most_common_df, x=1, y=0, orientation='h', color=1, text=1,
                     labels={'0': 'Words', '1': 'Count'}, template="plotly_dark")
        fig.update_traces(marker_color="cyan", textposition="outside", opacity=0.8)
        st.plotly_chart(fig, use_container_width=True)

        # --- Emoji Analysis ---
        st.markdown("## 😂 **Emoji Analysis**")
        emoji_df = helper.emoj_helper(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df.style.set_properties(**{'background-color': '#1E1E1E', 'color': 'white'}))
        with col2:
            fig = go.Figure(data=[go.Pie(labels=emoji_df[0].head(), values=emoji_df[1].head(),
                                         textinfo="label+percent", hole=0.4,
                                         marker=dict(colors=sns.color_palette("pastel")))])
            fig.update_layout(title_text="Top Used Emojis", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)

        # --- Weekly Activity Heatmap ---
        st.markdown("## 📆 **Weekly Activity Heatmap**")
        user_heat_map = helper.activity_heat_map(selected_user, df)
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.heatmap(
            user_heat_map,
            cmap="mako",  # Or try "rocket", "mako", "viridis" for a modern look
            annot=False,
            cbar=True,
            square=True,  # Ensures equal aspect ratio for a grid look
            linewidths=0  # Removes gaps between blocks
        )

        ax.set_title("Weekly Activity Heatmap", fontsize=16, fontweight='bold', pad=15, color='white')
        ax.set_facecolor('#1E1E1E')  # Background color
        st.pyplot(fig)

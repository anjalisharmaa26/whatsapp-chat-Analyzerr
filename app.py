import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

plt.rcParams['font.family'] = 'Segoe UI Emoji'

# Streamlit Page Configuration
st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")

# Global Matplotlib Settings for Dark Theme
plt.style.use('dark_background')
plt.rcParams.update({'axes.facecolor': '#1e1e1e', 'axes.edgecolor': 'white', 'xtick.color': 'white', 'ytick.color': 'white', 'text.color': 'white', 'axes.labelcolor': 'white'})

# Sidebar Configuration
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg", width=80)
st.sidebar.title("📊 WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("📂 Upload Your Chat File")

if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("👥 Select User", user_list)

    if st.sidebar.button("🔍 Analyze Chat"):
        st.markdown("<h1 style='text-align: center; color: white;'>📊 WhatsApp Chat Analysis</h1>", unsafe_allow_html=True)

        # --- Statistics Section ---
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        st.markdown("### 📌 Chat Insights")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("📝 Total Messages", num_messages)
        col2.metric("🗣️ Total Words", words)
        col3.metric("📷 Media Shared", num_media_messages)
        col4.metric("🔗 Links Shared", num_links)

        # --- Monthly Timeline ---
        st.markdown("### 📅 Monthly Chat Activity")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], marker="o", linestyle="-", color="lime", linewidth=2)
        ax.set_xlabel("Time", color='white')
        ax.set_ylabel("Messages", color='white')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # --- Daily Timeline ---
        st.markdown("### 📆 Daily Chat Trends")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], marker="o", linestyle="-", color="cyan", linewidth=2)
        ax.set_xlabel("Date", color='white')
        ax.set_ylabel("Messages", color='white')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # --- Activity Map ---
        st.markdown("### 📊 Activity Patterns")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🗓️ Most Active Days")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color="#4c72b0")
            ax.set_xlabel("Days", color='white')
            ax.set_ylabel("Messages", color='white')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:
            st.markdown("#### 📅 Most Active Months")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color="orange")
            ax.set_xlabel("Months", color='white')
            ax.set_ylabel("Messages", color='white')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # --- Weekly Activity Heatmap ---
        st.markdown("### 🔥 Weekly Activity Heatmap")
        user_heat_map = helper.activity_heat_map(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.heatmap(user_heat_map, cmap="coolwarm", linewidths=0.3, linecolor="white", cbar=True, annot=False)
        ax.set_xlabel("Hour", color='white')
        ax.set_ylabel("Day", color='white')
        st.pyplot(fig)

        # --- Busiest User Analysis (For Groups) ---
        if selected_user == 'Overall':
            st.markdown("### 👥 Most Active Users")
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns([2, 3])

            with col1:
                st.dataframe(new_df)

            with col2:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color="red")
                ax.set_xlabel("Users", color='white')
                ax.set_ylabel("Messages", color='white')
                plt.xticks(rotation=45)
                st.pyplot(fig)

        # --- Wordcloud ---
        st.markdown("### ☁️ WordCloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(df_wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

        # --- Most Common Words ---
        st.markdown("### 🔤 Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.barh(most_common_df[0], most_common_df[1], color="teal")
        ax.set_xlabel("Words", color='white')
        ax.set_ylabel("Frequency", color='white')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # --- Emoji Analysis ---
        st.markdown("### 😀 Emoji Analysis")
        emoji_df = helper.emoj_helper(selected_user, df)

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:

            fig, ax = plt.subplots(figsize=(6, 6))
            colors = sns.color_palette("pastel")

            wedges, texts, autotexts = ax.pie(
                emoji_df[1].head(),
                labels=[f"{emoji} ({count})" for emoji, count in zip(emoji_df[0].head(), emoji_df[1].head())],
                autopct="%0.2f%%",
                colors=colors,
                textprops={'fontsize': 11, 'color': 'magenta'},
                wedgeprops={'edgecolor': 'black'},
                pctdistance=0.85,
                shadow=True
            )

            # Set font to support emojis
            emoji_font = fm.FontProperties(fname=fm.findSystemFonts(fontpaths=None, fontext='ttf')[0])
            for text in texts:
                text.set_fontproperties(emoji_font)

            ax.set_title("Top Used Emojis", fontsize=18, fontweight='bold', pad=20, color='white')
            st.pyplot(fig)

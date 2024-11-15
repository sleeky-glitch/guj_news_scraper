import streamlit as st
# Search input
search_term = st.text_input("Enter search term (in Gujarati or English):", "પાણી")

if st.button("Search News"):
    if search_term:
        with st.spinner("Searching for news articles..."):
            # Scrape from both sources
            divya_bhaskar_articles = scrape_divya_bhaskar(search_term)
            gujarat_samachar_articles = scrape_gujarat_samachar(search_term)
            
            # Combine results
            all_articles = divya_bhaskar_articles + gujarat_samachar_articles
            
            if all_articles:
                # Convert to DataFrame
                df = pd.DataFrame(all_articles)
                
                # Display results
                st.success(f"Found {len(all_articles)} articles")
                
                # Display articles in tabs
                tab1, tab2 = st.tabs(["Table View", "Detailed View"])
                
                with tab1:
                    st.dataframe(df)
                    
                with tab2:
                    for idx, article in enumerate(all_articles, 1):
                        st.markdown(f"### {idx}. {article['Title (Gujarati)']}")
                        st.markdown(f"**English:** {article['Title (English)']}")
                        st.markdown(f"**Date:** {article['Date']}")
                        st.markdown(f"**Link:** [{article['Link']}]({article['Link']})")
                        st.markdown("---")
                
                # Download option
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "Download Results as CSV",
                    csv,
                    "news_articles.csv",
                    "text/csv",
                    key='download-csv'
                )
            else:
                st.warning("No articles found for the given search term.")
    else:
        st.warning("Please enter a search term.")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit • Data sourced from Divya Bhaskar and Gujarat Samachar")




def get_recommendations(keyword, df, cosine_sim, n_recommendations=5):
    """Get recommendations based on case-insensitive keyword search."""
    keyword = keyword.lower().strip()
    matching_mask = df['features'].str.contains(keyword, case=False, na=False)
    matching_products = df[matching_mask]
    
    if matching_products.empty:
        return [], []
    
    idx = matching_products.index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    recommended_indices = []
    seen_products = set()
    
    for i, score in sim_scores:
        product_name = df.iloc[i]['product_name']
        if product_name not in seen_products and not matching_mask.iloc[i]:
            recommended_indices.append(i)
            seen_products.add(product_name)
        if len(recommended_indices) >= n_recommendations:
            break
    
    matches = matching_products[['product_name', 'category', 'description']].to_dict('records')
    recommendations = df.iloc[recommended_indices][['product_name', 'category', 'description']].to_dict('records')
    return matches, recommendations

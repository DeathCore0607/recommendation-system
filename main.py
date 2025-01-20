from database import create_product_database
from similarity import prepare_recommendations
from recommendations import get_recommendations

def main():
    """Main function to run the recommendation system."""
    print("Initializing recommendation system...")
    df = create_product_database()
    cosine_sim = prepare_recommendations(df)
    
    while True:
        print("\n" + "="*50)
        print("Mobile Device Recommendation System")
        print("="*50)
        
        keyword = input("\nEnter a keyword to search (or 'quit' to exit): ").strip()
        
        if keyword.lower() == 'quit':
            break
            
        if not keyword:
            print("\nPlease enter a valid keyword.")
            input("\nPress Enter to continue...")
            continue
        
        matches, recommendations = get_recommendations(keyword, df, cosine_sim)
        
        if matches:
            print(f"\nContent - Based \"{keyword}\":")
            for i, product in enumerate(matches, 1):
                print(f"\n{i}. {product['product_name']} ({product['category']})")
                print(f"   {product['description']}")
            
            if recommendations:
                print(f"\nRecommendations for \"{keyword}\":")
                for i, product in enumerate(recommendations, 1):
                    print(f"\n{i}. {product['product_name']} ({product['category']})")
                    print(f"   {product['description']}")
        else:
            print(f"\nNo products found matching \"{keyword}\"")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

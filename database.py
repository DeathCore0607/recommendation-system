import pandas as pd

def create_product_database():
    """Create a database of real-world mobile devices and related products"""
    data = {
        "product_id": range(1, 51),  # 50 products
        "product_name": [
            # Smartphones
            "iPhone 15 Pro Max", "iPhone 15", "iPhone 14 Pro", "iPhone 14",
            "Samsung Galaxy S24 Ultra", "Samsung Galaxy S24+", "Samsung Galaxy S24",
            "Google Pixel 8 Pro", "Google Pixel 8", "Google Pixel 7a",
            "OnePlus 12", "OnePlus 11", "OnePlus Nord N30",
            "Samsung Galaxy A54", "Samsung Galaxy A34",
            
            # Tablets
            "iPad Pro 12.9", "iPad Air", "iPad mini",
            "Samsung Galaxy Tab S9 Ultra", "Samsung Galaxy Tab S9",
            
            # Accessories
            "Apple AirPods Pro", "Samsung Galaxy Buds2 Pro",
            "Apple MagSafe Charger", "Samsung 45W Charger",
            "iPhone 15 Pro Max Clear Case", "S24 Ultra Protective Case",
            
            # Smart Watches
            "Apple Watch Series 9", "Apple Watch Ultra 2",
            "Samsung Galaxy Watch 6", "Samsung Galaxy Watch 6 Classic",
            
            # Mobile Components
            "Qualcomm Snapdragon 8 Gen 3", "Apple A17 Pro Chip",
            "Samsung Exynos 2400", "Google Tensor G3",
            
            # Related Electronics
            "MacBook Pro 16", "MacBook Air 15",
            "Samsung Galaxy Book 3 Pro", "Dell XPS 13",
            "iPad Magic Keyboard", "Samsung Book Cover Keyboard",
            
            # Mobile Carriers/Services
            "T-Mobile 5G Plan", "Verizon Unlimited",
            "AT&T Mobile Share", "Google Fi Wireless",
            
            # Mobile Apps
            "Instagram Mobile App", "TikTok Mobile App",
            "WhatsApp Messenger", "Spotify Mobile",
            "Netflix Mobile App", "Mobile Banking App"
        ],
        "category": [
            # Categories for smartphones
            "Smartphone", "Smartphone", "Smartphone", "Smartphone",
            "Smartphone", "Smartphone", "Smartphone",
            "Smartphone", "Smartphone", "Smartphone",
            "Smartphone", "Smartphone", "Smartphone",
            "Smartphone", "Smartphone",
            
            # Categories for tablets
            "Tablet", "Tablet", "Tablet",
            "Tablet", "Tablet",
            
            # Categories for accessories
            "Accessory", "Accessory",
            "Accessory", "Accessory",
            "Accessory", "Accessory",
            
            # Categories for smartwatches
            "Smartwatch", "Smartwatch",
            "Smartwatch", "Smartwatch",
            
            # Categories for components
            "Component", "Component",
            "Component", "Component",
            
            # Categories for related electronics
            "Laptop", "Laptop",
            "Laptop", "Laptop",
            "Accessory", "Accessory",
            
            # Categories for services
            "Service", "Service",
            "Service", "Service",
            
            # Categories for apps
            "Mobile App", "Mobile App",
            "Mobile App", "Mobile App",
            "Mobile App", "Mobile App"
        ],
        "description": [
            # Descriptions for smartphones (first 15 products)
            "Pro-grade camera system, A17 Pro chip, titanium design",
            "Advanced dual-camera system, A16 Bionic chip",
            "48MP camera, Dynamic Island, A16 Bionic",
            "Dual-camera system, A15 Bionic chip",
            "200MP camera, Snapdragon 8 Gen 3, AI features",
            "50MP camera, Snapdragon 8 Gen 3, large display",
            "Dynamic AMOLED display, powerful performance",
            "Tensor G3 chip, advanced AI photography",
            "Compact flagship with powerful features",
            "Budget-friendly Google phone with great camera",
            "Snapdragon 8 Gen 3, 50MP camera, fast charging",
            "Flagship performance, Hasselblad cameras",
            "Budget 5G phone with good battery life",
            "Mid-range phone with great features",
            "Affordable phone with good performance",
            
            # Descriptions for tablets (next 5)
            "Liquid Retina XDR display, M2 chip",
            "M1 chip, 10.9-inch Liquid Retina display",
            "Compact tablet with A15 Bionic chip",
            "14.6-inch display, Snapdragon 8 Gen 2",
            "11-inch AMOLED display, powerful processor",
            
            # Descriptions for accessories (next 6)
            "Active noise cancellation, spatial audio",
            "Premium wireless earbuds with ANC",
            "15W wireless charging for iPhone",
            "Super fast charging for Galaxy devices",
            "Clear protective case with MagSafe",
            "Protective case with S Pen holder",
            
            # Descriptions for smartwatches (next 4)
            "Advanced health features, Always-On Retina display",
            "Rugged design, precision sports features",
            "Health tracking, sleep monitoring",
            "Classic design with rotating bezel",
            
            # Descriptions for components (next 4)
            "Leading mobile processor for Android",
            "Apple's most powerful mobile chip",
            "Samsung's flagship mobile processor",
            "Google's custom mobile processor",
            
            # Descriptions for related electronics (next 6)
            "Powerful laptop with M2 Pro/Max",
            "Thin and light with M2 chip",
            "Premium Windows laptop",
            "Compact premium Windows laptop",
            "Premium keyboard for iPad Pro",
            "Official keyboard cover for Tab S9",
            
            # Descriptions for services (next 4)
            "5G mobile plan with unlimited data",
            "Comprehensive wireless service",
            "Flexible data sharing plan",
            "Flexible mobile service with WiFi",
            
            # Descriptions for apps (next 6)
            "Photo sharing and social networking",
            "Short-form video platform",
            "Messaging and calling app",
            "Music streaming service",
            "Video streaming service",
            "Mobile banking and payments"
        ],
        "tags": [
            # Tags for each product...
            "apple iphone premium flagship mobile phone",
            "apple iphone mobile phone",
            "apple iphone premium mobile phone",
            "apple iphone mobile phone",
            "samsung android premium flagship mobile phone",
            "samsung android premium mobile phone",
            "samsung android mobile phone",
            "google android premium flagship mobile phone",
            "google android mobile phone",
            "google android budget mobile phone",
            "oneplus android premium flagship mobile phone",
            "oneplus android premium mobile phone",
            "oneplus android budget mobile phone",
            "samsung android midrange mobile phone",
            "samsung android budget mobile phone",
            
            # Tags for tablets
            "apple ipad tablet premium",
            "apple ipad tablet",
            "apple ipad tablet compact",
            "samsung android tablet premium",
            "samsung android tablet",
            
            # Tags for accessories
            "apple airpods wireless earbuds",
            "samsung wireless earbuds",
            "apple charging accessory",
            "samsung charging accessory",
            "apple phone case protection",
            "samsung phone case protection",
            
            # Tags for smartwatches
            "apple watch smartwatch wearable",
            "apple watch premium smartwatch",
            "samsung smartwatch wearable",
            "samsung premium smartwatch",
            
            # Tags for components
            "qualcomm processor chip mobile",
            "apple processor chip mobile",
            "samsung processor chip mobile",
            "google processor chip mobile",
            
            # Tags for related electronics
            "apple macbook laptop computer",
            "apple macbook laptop computer",
            "samsung laptop computer",
            "dell laptop computer",
            "apple ipad keyboard accessory",
            "samsung tablet keyboard accessory",
            
            # Tags for services
            "mobile carrier service network",
            "mobile carrier service network",
            "mobile carrier service network",
            "mobile carrier service network",
            
            # Tags for apps
            "social media mobile application",
            "social media mobile application",
            "messaging mobile application",
            "music streaming mobile application",
            "video streaming mobile application",
            "banking finance mobile application"
        ]
    }
    return pd.DataFrame(data)
from app import app
from models import db, Category
from random import choice as rc
from faker import Faker

with app.app_context():
    fake=Faker()
    
    Category.query.delete()
    categories=[]
    name_choices=['Maximalist', 'Joyful', 'Futuristic','College', 'Pastel', 'Proffessional']
    url_1=['https://d1csarkz8obe9u.cloudfront.net/posterpreviews/blue-bus-back-to-school-party-invite-story-design-template-1ede75df260b6ea35778e9d75e604377.jpg','https://d1csarkz8obe9u.cloudfront.net/posterpreviews/sunday-service-flyer-design-template-ae5d0482ab1f7e00d8c490a20793d701.jpg', 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/pink-fun-marketing-instagram-story-image-design-template-d5fe18b42f2e86386d3a2d1f5489fc10.jpg', 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/mustard-birthday-wish-for-him-instagram-video-design-template-1823a0534d19c6c0440d711f4596942a.jpg','https://d1csarkz8obe9u.cloudfront.net/posterpreviews/nft-flyer-template-design-94c97c4dc37dde98e9977c5c9ef094f3.jpg', 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/business-conference-design-template-770e36c220234c14dde2bed5561679e4.jpg']
    url_2=['https://d1csarkz8obe9u.cloudfront.net/posterpreviews/you-are-awesome-poster-design-template-838b7fc871b05e65b12fd3d602a1a77c.jpg','https://d1csarkz8obe9u.cloudfront.net/posterpreviews/vintage-jazz-concert-poster-design-template-e4806ad9b3d6f2f2f0e5d8709ae1d222.jpg', 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/upcoming-events-design-template-b7e70cc7363bf54732d0db2d75137e1a.jpg', 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/spring-break-design-template-2a026d896f0ef6d1cdac2d32f5a092f4.jpg']
    text=['Maximalist designs use vibrant colors, intricate patterns, and busy designs with lots of visual elements. Designs often use bold typography and dramatic imagery to create a visually stunning impact.', 'Joyful designs make use of bright colors, fun imagery or caricatures/cartoons, fun typography, and doodled elements', 'These designs are inspired by futuristic elements, incorporating sleek lines, metallic textures, and innovative visual elements.', 'These combine different images and elements to form a collage. These are commonly used for greeting cards, scrapbooks, and photo album designs.']
    
    
    for n in range(5):
        
        category=Category(name=rc(name_choices), description=rc(text), image_url_1=rc(url_1), image_url_2=rc(url_2))
        categories.append(category)
        
        db.session.add_all(categories)
        db.session.commit()
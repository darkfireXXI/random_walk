import json

import requests

url = "http://0.0.0.0:50051"
# url = "http://0.0.0.0:50051/register"
# url = "http://127.0.0.1:50051/"

url = "http://0.0.0.0:50051/category-group/list"

r = requests.get(url)
# payload = {"user_name": "user_name", "password": "password", "email": "email"}
# r = requests.post(url, data=json.dumps(payload))
print(r)
print(r.text)
# print(r.json())


# python3 -m http.server 8000
# python3 -m db.seed -i


# architecture_urls = [
#     "https://www.nytimes.com/2021/11/18/arts/design/nyc-subway-architecture-history.html",
#     "https://www.archinect.com/news/article/150146/ai-and-architecture-the-next-frontier",
#     "https://www.dezeen.com/2020/02/14/futuristic-sustainable-architecture-design-green-buildings/",
#     "https://www.archaeology.org/issues/339-2003/digs/3708-digs-greece-architecture",
#     "https://www.theguardian.com/artanddesign/2020/dec/01/how-architecture-can-help-us-survive-climate-crisis",
#     "https://www.designboom.com/architecture/taichung-cultural-centre-architecture-02-03-2022/",
#     "https://www.bbc.com/culture/article/20190425-the-aesthetics-of-brutalism",
#     "https://www.architecturaldigest.com/story/sustainable-architecture-for-climate-change",
#     "https://www.metalocus.es/en/news/exploring-beautiful-but-forgotten-architecture-detroit",
#     "https://www.e-architect.com/articles/architectural-models",
#     "https://www.dezeen.com/2022/07/12/office-architecture-future-design-covid-workplace/",
#     "https://www.archdaily.com/924557/interactive-architecture-innovative-building-technologies-that-respond-to-the-human-environment",
#     "https://www.npr.org/2021/04/22/988506432/the-rise-of-tiny-homes-and-why-they-are-here-to-stay",
#     "https://www.tate.org.uk/art/artworks/hayward-the-shard-london-tate-studio-artwork",
#     "https://www.dezeen.com/2021/04/08/future-office-design-workspaces/",
#     "https://www.theatlantic.com/technology/archive/2020/12/why-architecture-is-key-modern-city-survival/617800/",
#     "https://www.moma.org/collection/works/80163",
#     "https://www.architecturaldigest.com/story/mid-century-modern-buildings",
#     "https://www.smithsonianmag.com/smart-news/how-frank-lloyd-wrights-guggenheim-changed-museum-architecture-180956804/",
#     "https://www.artsy.net/article/artsy-editorial-inside-architecture-metaverse"
# ]


# architecture_urls.extend([
#     # Architectural Digest: Tour a Reimagined Hollywood Regency-style House in Dallas
#     "https://www.architecturaldigest.com/gallery/tour-a-reimagined-hollywood-regency-style-house-in-dallas",
#     # Wallpaper*: What is DeafSpace and how can it enhance architecture for everyone?
#     "https://www.wallpaper.com/architecture/deafspace-sense-centric-architecture",
#     # Vanity Fair: "I Will Never Give Up Creating, Because to Create Is to Live": An Interview With Architect Tadao Ando
#     "https://www.vanityfair.com/style/story/interview-with-architect-tadao-ando",
#     # Financial Times: The Yale Center for British Art remains as fiercely contemporary as ever
#     "https://www.ft.com/content/4e249a2d-24e1-4f5b-ad35-7df8e6386de6",
#     # Country Life: Sir Edwin Lutyens and the architecture of the biggest bank in the world
#     "https://www.countrylife.co.uk/architecture/sir-edwin-lutyens-and-the-architecture-of-the-biggest-bank-in-the-world",
#     # Dezeen: Designboom - Daily web magazine covering industrial design, architecture, and art
#     "https://www.designboom.com/",
#     # ArchDaily: Global architecture news, projects, and competitions
#     "https://www.archdaily.com/",
#     # Design Observer: Articles on design, architecture, and urbanism
#     "https://designobserver.com/",
#     # The Architect's Newspaper: News and analysis on architecture and urbanism
#     "https://www.archpaper.com/",
#     # Metropolis Magazine: Architecture, culture, and design magazine
#     "https://www.metropolismag.com/",
#     # Life of an Architect: Blog by Bob Borson on architectural practice and design
#     "https://www.lifeofanarchitect.com/",
#     # Visualizing Architecture: Architectural visualization and design blog
#     "https://www.visualizingarchitecture.com/",
#     # Contemporist: Contemporary architecture and design blog
#     "https://www.contemporist.com/",
#     # Daily Dose of Architecture: Daily architectural inspiration and news
#     "https://www.dailydoseofarchitecture.com/",
#     # Biber: Architectural design firm with a focus on innovative solutions
#     "https://www.biber.com/",
#     # ArchitectureAU: Australian architecture and design news
#     "https://architectureau.com/",
#     # Dwell: Design and architecture magazine featuring modern homes
#     "https://www.dwell.com/",
#     # Archinect: Architecture news, forums, and job listings
#     "https://www.archinect.com/",
#     # The Local Project: Australian architecture and design magazine
#     "https://www.thelocalproject.com.au/",
#     # Design Milk: Interior design, architecture, modern furniture, and art blog
#     "https://design-milk.com/category/architecture/",
#     # The Modern House: Journal featuring architecture and design stories
#     "https://www.themodernhouse.com/journal/category/architecture/",
#     # My Modern Met: Art, architecture, photography, and design blog
#     "https://mymodernmet.com/category/architecture/",
#     # Decoist: Interior design and architecture blog
#     "https://www.decoist.com/dream-houses/",
#     # Architizer: Architectural projects, products, and competitions platform
#     "https://architizer.com/blog/",
#     # The Architect's Newspaper: Architecture news and events
#     "https://www.archpaper.com/",
#     # Designboom: Daily web magazine covering industrial design, architecture, and art
#     "https://www.designboom.com/",
#     # Life of an Architect: Blog by Bob Borson on architectural practice and design
#     "https://www.lifeofanarchitect.com/",
#     # Visualizing Architecture: Architectural visualization and design blog
#     "https://www.visualizingarchitecture.com/",
#     # Contemporist: Contemporary architecture and design blog
#     "https://www.contemporist.com/",
#     # Daily Dose of Architecture: Daily architectural inspiration and news
#     "https://www.dailydoseofarchitecture.com/",
#     # Biber: Architectural design firm with a focus on innovative solutions
#     "https://www.biber.com/",
#     # ArchitectureAU: Australian architecture and design news
#     "https://architectureau.com/",
#     # Dwell: Design and architecture magazine featuring modern homes
#     "https://www.dwell.com/",
#     # Archinect: Architecture news, forums, and job listings
#     "https://www.archinect.com/",
#     # The Local Project: Australian architecture and design magazine
#     "https://www.thelocalproject.com.au/",
#     # Design Milk: Interior design, architecture, modern furniture, and art blog
#     "https://design-milk.com/category/architecture/",
#     # The Modern House: Journal featuring architecture and design stories
#     "https://www.themodernhouse.com/journal/category/architecture/",
#     # My Modern Met: Art, architecture, photography, and design blog
#     "https://mymodernmet.com/category/architecture/",
#     # Decoist: Interior design and architecture blog
#     "https://www.decoist.com/dream-houses/",
#     # Architizer: Architectural projects, products, and competitions platform
#     "https://architizer.com/blog/",
#     # The Architect's Newspaper: Architecture news and events
#     "https://www.archpaper.com/",
#     # Designboom: Daily web magazine covering industrial design, architecture, and art
#     "https://www.designboom.com/",
#     # Life of an Architect: Blog by Bob Borson on architectural practice and design
#     "https://www.lifeofanarchitect.com/",
#     # Visualizing Architecture: Architectural visualization and design blog
#     "https://www.visualizingarchitecture.com/",
#     # Contemporist: Contemporary architecture and design blog
#     "https://www.contemporist.com/",
#     # Daily Dose of Architecture: Daily architectural inspiration and news
#     "https://www.dailydoseofarchitecture.com/",
#     # Biber: Architectural design firm with a focus on innovative solutions
#     "https://www.biber.com/",
#     # ArchitectureAU: Australian architecture and design news
#     "https://architectureau.com/",
#     # Dwell: Design and architecture magazine featuring modern homes
#     "https://www.dwell.com/",
#     # Archinect: Architecture news, forums, and job listings
#     "https://www.archinect.com/",
#     # The Local Project: Australian architecture and design magazine
#     "https://www.thelocalproject.com.au/",
#     # Design Milk: Interior design, architecture, modern furniture, and art blog
#     "https://design-milk.com/category/architecture/",
#     # The Modern House: Journal featuring architecture and design stories
#     "https://www.themodernhouse.com/journal/category/architecture/",
#     # My Modern Met: Art, architecture, photography, and design blog
#     "https://mymodernmet.com/category/architecture/",
#     # Decoist: Interior design and architecture blog
#     "https://www.decoist.com/dream-houses/",
#     # Architizer: Architectural projects, products, and competitions platform
#     "https://architizer
# ::contentReference[oaicite:0]{index=0}

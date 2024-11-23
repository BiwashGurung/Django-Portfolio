from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects (request):
    projects_show=[
        {
            'title': "Biwash's Culinary Haven",
            'path': 'images/culinary.png',
            'live_url':'https://biwashgurung.github.io/Chef-BiwashGurung-Website/',
        },
        {
            'title': 'DG Clothing Store',
            'path': 'images/DGClothing.png',
            'live_url':'https://biwashgurung.github.io/Ecommerce-Online-Clothing-Store/',

        },

        {
            'title': 'PUBG Website',
            'path': 'images/pubg.png',
            'live_url':'https://biwashgurung.github.io/PUBG-Website/',

        },
        {
            'title': 'Personal Portfolio Design',
            'path': 'images/portfolio.png',
            'live_url':'https://biwashgurung.github.io/Portfolio-Design/',

        },

         {
            'title': 'Dexys Store',
            'path': 'images/Dexys Sotre.png',
            'live_url':'https://biwashgurung.github.io/Dexy-s-Store/',

        },
          {
            'title': 'Shringar With Dexys Style',
            'path': 'images/Shringar.png',
            'live_url':'https://biwashgurung.github.io/Shringar-with-dexys-style/',

        },
         {
            'title': 'Aqua Bazzar',
            'path': 'images/Aqua.png',
            'live_url':'https://biwashgurung.github.io/Aquarium-Store/',

        },
                  {
            'title': 'PokharaWebMasters',
            'path': 'images\Pokhara Web.png',
            'live_url':'https://biwashgurung.github.io/PokharaWebMasters/',

        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})

def experience(request):
    experience = [
        {
            "company": "Dexy Co.",
            "position": "FullStack Developer",
            "start_date": "2024/01/03",
            "end_date": "Present",
        },
        {
            "company": "PokharaWebMasters",
            "position": "Python Developer",
            "start_date": "2023/06/07",
            "end_date": "2023/12/27",
        },
        {
            "company": "CodeHub IT and Solution",
            "position": "Jr. Python Developer",
            "start_date": "2022/03/01",
            "end_date": "2023/05/30",
        },
    ]
    return render(request, "experience.html", {"experience": experience})

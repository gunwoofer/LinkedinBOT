from linkedin_api import Linkedin
import config

api = Linkedin(config.login["username"], config.login["password"])


def search_recruiters():
    results = api.search_people(keywords=config.KEYWORDS, regions=config.CITY, limit=config.NBR_RECHERCHE)

    profils = []
    for people in results:
        profil = api.get_profile(people["public_id"])
        profils.append(profil)
    return profils

def ask_internship():
    pass

def main():
    if (config.OBJECTIF == "ADDRECRUITERS"):
        recruiters = search_recruiters()
        

    elif ( config.OBJECTIF == "SENDMESSAGES"):
        pass


if __name__ == "__main__":
    main()


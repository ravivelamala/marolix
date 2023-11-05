# create a careerpage class inside that we have to create two classes,
# one class is for admin, to add jobpost and see the number of applications with detailsand second class is for user to see number of jobs and apply for job 
class CareerPage:
    def __init__(self):
        self.job_posts = []
        self.applications = []

    class Admin:
        def __init__(self, career_page):
            self.career_page = career_page

        def add_job_post(self, title, description):
            job_post = {
                "title": title,
                "description": description,
                "applications": []
            }
            self.career_page.job_posts.append(job_post)

        def view_applications(self):
            for job_post in self.career_page.job_posts:
                print(f"Job Title: {job_post['title']}")
                print("Applications:")
                for application in job_post["applications"]:
                    print(application)
                print()

    class User:
        def __init__(self, career_page):
            self.career_page = career_page

        def view_jobs(self):
            print("Available Jobs:")
            for i, job_post in enumerate(self.career_page.job_posts, start=1):
                print(f"{i}. {job_post['title']}")

        def apply_for_job(self, job_index, name, email, resume):
            if 0 <= job_index < len(self.career_page.job_posts):
                job_post = self.career_page.job_posts[job_index]
                application = {
                    "name": name,
                    "email": email,
                    "resume": resume
                }
                job_post["applications"].append(application)
                self.career_page.applications.append(application)
                print(f"Applied for job: {job_post['title']}")

career_page = CareerPage()
admin = CareerPage.Admin(career_page)
user1 = CareerPage.User(career_page)
user2 = CareerPage.User(career_page)

admin.add_job_post("Software Developer", "Full-stack developer position")
admin.add_job_post("Data Analyst", "Analyze and interpret data")

user1.view_jobs()
user1.apply_for_job(0, "John Doe", "john@example.com", "Resume for Software Developer")

user2.view_jobs()
user2.apply_for_job(1, "Jane Smith", "jane@example.com", "Resume for Data Analyst")

admin.view_applications()

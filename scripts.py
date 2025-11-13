from datacenter.models import Schoolkid,Teacher,Mark, Chastisement
import random_lesson

def get_schoolkid(name):
    schoolkid = Schoolkid.objects.get(full_name=name)
            print(f"✅ Найден ученик: {schoolkid.full_name}")
            return schoolkid
        except Schoolkid.DoesNotExist:
            print(f"Ученика с таким именем '{name}' нет в базе")
            return None
        except Schoolkid.MultipleObjectsReturned:
            print(f"Найдено несколько учеников с именем '{name}'")
            print("Уточните имя ученика")
            return None


def fix_marks(schoolkid):
  	updated = Mark.objects.filter(points__lt=4,schoolkid=schoolkid).update(points=5)


def remove_chastisement(schoolkid):
  	child_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
  	child_chastisement.delete()


def add_commendation(schoolkid):
	our_lesson = list(Lesson.objects.filter(
        subject__title='Музыка', 
        year_of_study=6, 
        group_letter='А'
    ).order_by('-date'))

    random_lesson = random.choice(our_lesson)

	Commendation.objects.create(
    	teacher=random_lesson.teacher, 
    	subject=random_lesson.subject, 
    	created=random_lesson.date, 
    	text='Ты сегодня прыгнул выше головы!', 
    	schoolkid=schoolkid
    	)
# running in the context of a web2py shell
import json, datetime, sys


def createUser(username, password, fname, lname, email, course_name, section, instructor=False):
    cinfo = db(db.courses.course_name == course_name).select().first()
    if not cinfo:
        raise ValueError("Course {} does not exist".format(course_name))
    pw = CRYPT(auth.settings.hmac_key)(password)[0]
    uid = db.auth_user.insert(username=username, password=pw, first_name=fname,
                        last_name=lname, email=email,
                        course_id=cinfo.id, course_name=course_name, active='T',
                        created_on=datetime.datetime.now() )

    db.user_courses.insert(user_id=uid, course_id=cinfo.id)

    ###From Original makeuser.py
    #sect = db((db.sections.course_id == cinfo.id) &
    #          (db.sections.name == 'default')).select(db.sections.id).first()
 


    ###Checks to see if the section exists and adds it the db if it does not.
    sect = db((db.sections.course_id == cinfo.id) &
              (db.sections.name == section)).select(db.sections.id).first()

    if not sect:
        db.sections.update_or_insert(name = str(section), course_id = cinfo.id)
        sect = db((db.sections.course_id == cinfo.id) &
                  (db.sections.name == str(section))).select(db.sections.id).first()
        
    db.section_users.update_or_insert(auth_user=uid, section=sect)

    if instructor:
        irole = db(db.auth_group.role == 'instructor').select(db.auth_group.id).first()
        db.auth_membership.insert(user_id=uid, group_id=irole)
        db.course_instructor.insert(course=cinfo.id, instructor=uid)

    db.commit()

if '--userfile' in sys.argv:
    # find the file (.csv) iterate over each line and call createUser
    pass
else:
    # user info will come in as a json object
    userinfo = json.loads(os.environ['RSM_USERINFO'])
    createUser(userinfo['username'], userinfo['password'], userinfo['first_name'],
               userinfo['last_name'], userinfo['email'], userinfo['course'], userinfo['section'],
               userinfo['instructor'])

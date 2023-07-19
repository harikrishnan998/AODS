import pyrebase.pyrebase

def rto(no,database):
    # database.child("RTO").child("KL12F9966").child("num").set("1")
    db=database.child("RTO").get()
    if no in db.val():
        n=database.child("RTO").child(no).child("num").get()
        return n.val()
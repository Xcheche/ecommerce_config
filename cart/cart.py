class Cart():
    #Old User
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('session_key')

        #New User

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


            self.cart = cart
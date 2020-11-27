   $(document).ready(function(){

            $('#Button').click(function(){
                $('#loginModal').modal('show');

            
            });
        
            $('#loginclose').click(function(){
                if($('#loginclose').children('button').hasClass('close')){
                    $('#loginModal').modal('hide') ;
                    }

            });
            $('#logincancel').click(function(){
                if($('#logincancel').children('button')){
                    $('#loginModal').modal('hide') ;
                    }

            });
            $('#Buttonsign').click(function(){
                $('#signupModal').modal('show');

            
            });

        
            $('#signupclose').click(function(){
                if($('#signupclose').children('button').hasClass('close')){
                    $('#signupModal').modal('hide') ;
                    }

            });
            $('#signupcancel').click(function(){
                if($('#signupcancel').children('button')){
                    $('#signupModal').modal('hide') ;
                    }

            });



           

            
 }); 
function submitResponse(){

    var response = document.getElementById("id1").value;
    var sessionID = document.getElementById("id2").value;
    var username = document.getElementById("id3").value;
    var questionNumber = document.getElementById("id4").value;
    
    if(response.length == 0 || sessionID.length == 0 || username.length ==0){
      alert('One or many boxes are empty!')
    }else{
      const session_lbl = window.location.href.indexOf("session/") + 8
      const session_id = window.location.href.substring(session_lbl)
      const user_id = '{{user.id}}'
      const Url = 'http://classroomplus.herokuapp.com/frq/'+sessionID+'/'+questionNumber + '/'+ user_id;
      
      
        const data = {
       'session_id' : 'ABCD1234',
        'response' : respoonse
        }
       
        $.post(Url,data,function(data,status){
            console.log('${data} and status is ${status}');
        });
  }

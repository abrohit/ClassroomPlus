

function myFunction(){

    const session_lbl = window.location.href.indexOf("makequiz/") + 9
    const session_id = window.location.href.substring(session_lbl)
    console.log(session_id.replace(/\//g,'-'))
    var question = document.getElementsByClassName("input-box");
    var typeOfQuestion = document.querySelector("select").value;

    var status =  true
     for(var x=0; x<question.length; x++){
        console.log(question[x].value +" "+ x)
        if(question[x].value.length == 0){
        status = false
        alert('One or many boxes are empty')
        break;
        }
     }

    //not sure how to acess user id and username
  console.log(status)
    if(status){
  const Url='http://classroomplus.herokuapp.com/question/'+session_id.replace(/\//g,'-')+ '/' + question[0].value;
  console.log(Url)
        const data={
            session_id: ""+session_id.replace(/\//g,'-'),
            question: ""+question[1].value,
            q_type: ""+typeOfQuestion,
            correct: ""+question[2].value,
            wrong: ""+question[3].value
        }

      try{
       $.post(Url, data, function(data, status){
          console.log('${data} and status is ${status}')
       });
      }catch{
        alert('Question already exists in this lecture with that number')
      }


    }

    for(var x=0; x<question.length; x++){
      question[x].value = ''
    }

}

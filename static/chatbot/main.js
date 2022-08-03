document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.getElementById("input");
    inputField.addEventListener("keydown", (e) => {
      if (e.code === "Enter") {
        let input = inputField.value;
        inputField.value = "";
        
        $.ajax({
          url: "",
          type: "get",
          contentType: "application/json",
          data: {
            input_text: input,
          },
          success: function (response) {
            
            addChat(input, response);
          }
        })
      }
    });
  });
  
  function addChat(input, response) {
    c = 0

    const messagesContainer = document.getElementById("messages");
  
    let userDiv = document.createElement("div");
    userDiv.id = "user";
    userDiv.className = "user response";
    userDiv.innerHTML = `<span>${input}</span><img src="/static/chatbot/user.png" class="avatar">`;
    messagesContainer.appendChild(userDiv);
    

    let botDiv = document.createElement("div");
    let botImg = document.createElement("img");
    let botText = document.createElement("span");


    botDiv.id = "bot";
    botImg.src = "static/chatbot/bot-mini.png";
    botImg.className = "avatar";
    botDiv.className = "bot response";
    botText.innerText = "Digitando...";
    
    botDiv.appendChild(botImg);
    botDiv.appendChild(botText);
    messagesContainer.appendChild(botDiv);

    messagesContainer.scrollTop = messagesContainer.scrollHeight - messagesContainer.clientHeight;
  
    // Fake delay to seem "real"
    setTimeout(() => {
      
      botText.innerText = response.res;
      //textToSpeech(response.res);
    }, 2000);
    
    /*
    if (typeof response.res[0][0] == 'object') {
        
        let list = document.createElement("ul");

        for (i in response.res[0]) {
            let item = document.createElement("li");
            item.innerText = response.res[0][c]

            list.appendChild(item)
            c += 1;
        }
        messagesContainer.appendChild(list);
        
        

        messagesContainer.scrollTop = messagesContainer.scrollHeight - messagesContainer.clientHeight;
        setTimeout(() => {   
            botText.innerText = response.res.at(-1);
            //textToSpeech(response.res);
        }, 2000);
    
    }
    else {
      */  
      // Keep messages at most recent
      
   //}   
}
//creating the object of XMLHttpRequest class
xhr=new XMLHttpRequest();

//preparing the ajax request call
xhr.open('GET',"http://127.0.0.1:8000/homeall/",true)


//handling the data on load
xhr.onload = ()=>{
    if xhr.status ==== 200{
        js_obj=JSON.parse(xhr.responseText);
        console.log(js_obj);
    }
}

//sending the ajax request
xhr.send()


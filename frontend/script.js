async function predictJob(){

    const text=document.getElementById("jobText").value;

    if(text===""){

        alert("Please paste Job Description");

        return;
    }

    document.getElementById("prediction").innerHTML="Analyzing...";

    document.getElementById("confidence").innerHTML="";

    const response=await fetch("http://127.0.0.1:5000/predict",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            job_description:text

        })

    });

    const result=await response.json();

    document.getElementById("prediction").innerHTML=result.prediction;

    document.getElementById("confidence").innerHTML=

        "Confidence : "+result.confidence+" %";

}
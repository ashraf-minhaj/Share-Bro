/**
 * File Sharing application using AWS services.
 * 
 * This project is being made to practice and demonstrate devops practices.
 * 
 * author: ashraf minhaj
 * mail  : ashraf_minhaj@yhaoo.com
 */

var API = "http://127.0.0.1:5000"

function get_presigned_url(file_name) {
    // var url = API + "/getpresignedurl/" + file_name
    var url = API + "/getpresignedurl/" + "file.png"

    console.log(url)

    fetch(url, 
        {
            method:'GET'
        }).then(response=>{
            // console.log(response.json())
            return response.json()
        }).then(data=> 
            // this is the data we get after putting our data,
            console.log(data)
            );
};

function upload_file(url, file) {
    fetch(url, 
        {
            method: 'PUT',
            mode: 'cors',
            body: file
        });
};

function upload(){
    /* gets presigned url and uploads file to s3 */
    var file_selector   = document.getElementById("file-selector")
    var file_name       = file_selector.value
    var file            = file_selector.files[0]
    var sgn_url         = 'nothing'

    if (file_name == "") {
        alert("Select a file, bro don't share empty files")
        return 0;
    }

    console.log("Uploading file", file_name);
    console.log(file)

    console.log("Getting presigned URL");
    sgn_url = get_presigned_url(file_name)
    console.log(sgn_url)

    console.log("uploading file to s3");
    upload_file(sgn_url, file)

    // show object cloudfront url on text input
    document.getElementById("url").value = "cdn.com/"+file_name;
    console.log("url set")
    // alert("File uploaded, copy the url and share to your bros!!!")
};

function copy(){
    /* copies url from input field to clipboard */
    console.log("copying url");

    var url_input_field = document.getElementById("url");

    url_input_field.select();
    url_input_field.setSelectionRange(0, 99999); // for mobile devices, as w3 school says (hehe)

    navigator.clipboard.writeText(url_input_field.value)
    alert("Copied URL, ready to share with bros!")
};

function download(){
    /* given a valid cloudfront URL it get's the files */
    console.log("Downloading file..")
}
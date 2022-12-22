/**
 * File Sharing application using AWS services.
 * 
 * This project is being made to practice and demonstrate devops practices.
 * 
 * author: ashraf minhaj
 * mail  : ashraf_minhaj@yhaoo.com
 */

var API = "http://127.0.0.1:5000"

async function get_presigned_url(file_name) {
    // var url = API + "/getpresignedurl/" + file_name
    var url = API + "/getpresignedurl/" + "file2.png"
    console.log(url)

    let res = await fetch(url);
    let d = res.json()
    console.log(d)
    return d
};

async function upload_file(url, file) {
    await fetch(url, 
        {
            method: 'PUT',
            mode: 'cors',
            body: file
        });
};

async function upload(){
    /* gets presigned url and uploads file to s3 */
    var file_selector   = document.getElementById("file-selector")
    var file_name       = file_selector.value
    var file            = file_selector.files[0]
    let res;
    let sgn_url;

    if (file_name == "") {
        alert("Select a file, bro don't share empty files")
        return 0;
    }

    console.log("Uploading file", file_name);
    console.log(file)

    console.log("Getting presigned URL");
    res = await get_presigned_url(file_name);
    sgn_url = await res['signedUrl']

    console.log("This is the data I get")
    console.log(sgn_url)

    upload_file(sgn_url, file);

    // show object cloudfront url on text input
    // document.getElementById("url").value = "cdn.com/"+file_name;
    document.getElementById("url").value = sgn_url;
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
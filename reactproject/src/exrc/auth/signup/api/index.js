const server = `http://localhost:8000`
const signupService = {
    apiSignUp, apiSignUpPostMethodByPromise
}
function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
}
async function apiSignUp(){
    const res = await 
    fetch(`${server}/exrc/auth/exrc_users`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    alert('더미 사용자 생성 ::: '+res)
    // return Promise.resolve(res);
}

async function apiSignUpPostMethodByPromise(){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify()
    }
    fetch(`${server}/exrc/auth/exrc_users`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

export default signupService
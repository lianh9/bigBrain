//Finding HTML elements by CSS Selectors h2
const setTime = document.querySelector('h2')
//set pomodoro time to 25 min and break time to 5 min
let pomodoro = 1500;
let breakTime = 300;
displayTime(pomodoro);
// Add a click listener to the pomodoro button, once user clicks
// The pomodoro timer will start
const setButton = document.getElementById("start");
setButton.addEventListener("click",function startPomodoro(){
    pomodoroTimer(pomodoro);
});
/**
 * Function to set the time interval for the pomodoro timer
 * and end the pomodoro timer when timer finishes
 * @param {s} second 
 */
function pomodoroTimer(second){
const timer = setInterval (()=>{
    pomodoro--;
    displayTime(pomodoro);
    if(pomodoro <= 0 || pomodoro < 1){
        endTimer();
        breakTimer(breakTime);
        clearInterval(timer);
    }
},1000)
}
/**
 * Function to set the time interval for the break timer
 * and end the break timer when break timer finishes
 * @param {s} second 
 */
function breakTimer(second){
    const timer = setInterval (()=>{
        breakTime--;
        displayTime(breakTime);
        if(breakTime <= 0 || breakTime < 1){
            endBreakTimer();
            clearInterval(timer);
        }
    },1000)
    }
/**
 * Funtion to display time in the format of 00:00
 * and calculate the minites and second  
 * @param {*} second 
 */
function displayTime(second){
    const min = Math.floor(second / 60);
    const sec = Math.floor(second % 60);
    m=format(min);
    s=format(sec)
    setTime.innerHTML = m + ":" + s;
}
/**
 * Function to format the time, when minites or seconds 
 * are less than 10, add 0 in front of them
 * @param {*} temp 
 * @returns temp
 */
function format(temp){
    if (temp < 10){
        temp = '0'+ temp;
    }
    return temp;
}
/**
 * Functions to end the pomodoro timer and display text 
 * Time for break on the website
 */
function endTimer(){
    setTime.innerHTML='Time for break';
}
/**
 * Functions to end the break timer and display text 
 * End for break on the website
 */
function endBreakTimer(){
    setTime.innerHTML='End for break';
}

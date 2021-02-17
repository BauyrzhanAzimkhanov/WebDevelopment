let arrayOfTasks = new Array();
let curId = 0;

function addNewTask()
{
    let curTask = document.getElementById("myInput").value;
    let task = document.createElement('div');
    task.id = curId++;
    task.className = "tasks";
    task.innerHTML = '<input type="checkbox" onclick="checking(' + task.id + "," + 0 + ')"><span id="' + "span" + task.id + '" class="taskNames">'+curTask+'</span><a class="trash" onclick="removeTask(' + task.id + ')">🗑️</a>'
    let container = document.querySelector("#container");
    document.getElementById("myInput").value = "";
    arrayOfTasks.push(task);
    container.appendChild(task);
}
function removeTask(myId)
{
    
    let container = document.querySelector("#container");
    for(let i = 0; i < arrayOfTasks.length; i++)
    {
        if(arrayOfTasks[i].id == myId)
        {
            container.removeChild(arrayOfTasks[i]);
            arrayOfTasks.splice(i,1);
            break;
        }

    }

    
}
function checking(myId, cntOfChecking)
{
    
    let mySpan = document.querySelector("#span" + myId);
    if(mySpan.style.textDecoration == "line-through")
    {
        mySpan.style.textDecoration = "none";
    }
    else
    {  
        mySpan.style.textDecoration = "line-through";
    }
    // mySpan.cntOfChecking++;
}
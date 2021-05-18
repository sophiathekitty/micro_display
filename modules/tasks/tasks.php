<?php
function AutomateTasks(){
    echo "Automate Task Notification<br>";
    // this will need to be extended to automate local tasks
}
function CompleteTask($task_id,$completed_by){
    UpdateTask($task_id,[
        'completed_by'=>$completed_by,
        'completed'=>date("Y-m-d H:i:s")
    ]);
    return LoadTask($task_id);
}
function TaskRoomNotification($room_id){
    $tasks = LoadAllTasksRoom($room_id);
    $notifications = [];
    $soon = time()+(60*5);
    $later = time()-(60*240);


    foreach($tasks as $task){
        if(is_null($task['due']) || strtotime($task['due']) < $soon){
            if(is_null($task['completed']) || strtotime($task['completed']) > $later){
                $notifications[] = $task;
            }
        }
    }
    return $notifications;
}
?>
<?php
require_once("../../includes/main.php");
$data = [];
if(isset($_GET['room_id'],$_GET['notifications'])){
    // load notifications for room
    $data['notifications'] = TaskRoomNotification($_GET['room_id']);
} elseif(isset($_GET['room_id'], $_GET['active'])){
    // get all the active tasks for a room
    $data['tasks'] = LoadActiveTasksRoom($_GET['room_id']);
} elseif(isset($_GET['task_id'], $_GET['completed_by'])){
    // complete a task
    $data['task'] = CompleteTask($_GET['task_id'],$_GET['completed_by']);
} elseif(isset($_GET['room_id'])){
    // get all tasks for room
    $data['tasks'] = LoadAllTasksRoom($_GET['room_id']);
} elseif(isset($_GET['active'])){
    // get all active tasks
    $data['tasks'] = LoadActiveTasks();
} else {
    // get all tasks
    $data['tasks'] = LoadAllTasks();
}
OutputJson($data);
?>
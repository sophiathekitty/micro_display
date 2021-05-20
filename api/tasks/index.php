<?php
require_once("../../includes/main.php");
$tasks = TaskManager::GetInstance();
$data = [];
if(isset($_GET['room_id'],$_GET['notifications'])){
    // load notifications for room
    $data['notifications'] = TaskManager::TaskRoomNotification($_GET['room_id']);
} elseif(isset($_GET['room_id'], $_GET['active'])){
    // get all the active tasks for a room
    $data['tasks'] = $tasks->LoadActiveTasksRoom($_GET['room_id']);
} elseif(isset($_GET['task_id'], $_GET['completed_by'])){
    // complete a task
    $data['task'] = $tasks->CompleteTask($_GET['task_id'],$_GET['completed_by']);
} elseif(isset($_GET['room_id'])){
    // get all tasks for room
    $data['tasks'] = $tasks->LoadAllTasksRoom($_GET['room_id']);
} elseif(isset($_GET['active'])){
    // get all active tasks
    $data['tasks'] = $tasks->LoadActiveTasks();
} else {
    // get all tasks
    $data['tasks'] = $tasks->LoadAll();
}
OutputJson($data);
?>
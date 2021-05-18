<?php

function PingUser($user_id){
    $time = date("Y-m-d H:i:s");
    clsDB::$db_g->safe_update("users",["last_login"=>$time],['id'=>$user_id]);
}
function PingUserLogin($login_id){
    $time = date("Y-m-d H:i:s");
    clsDB::$db_g->safe_update("user_login",["modified"=>$time],['id'=>$login_id]);
}
function GetUserName($username){
    $user = clsDB::$db_g->select("SELECT * FROM `users` WHERE `username` = '$username';");
    if(count($user)){
        return $user[0];
    }
    return NULL;
}
function CreateUser($username,$password){
    $id = clsDB::$db_g->safe_insert("users",["username"=>$username,"password"=>$password]);
    return GetUserById($id);
}

function GetUserById($user_id){
    $user = clsDB::$db_g->select("SELECT * FROM `users` WHERE `id` = '$user_id';");
    if(count($user)){
        return $user[0];
    }
    return NULL;
}
function GetLoginUserById($id){
    $login = clsDB::$db_g->select("SELECT * FROM `user_login` WHERE `id` = '$id';");
    if(count($login)){
        return $login[0];
    }
    return NULL;
}
function GetAllLoginUserById($id){
    return clsDB::$db_g->select("SELECT * FROM `user_login` WHERE `id` = '$id';");
}
function GetLoginUserByIP($ip){
    $login = clsDB::$db_g->select("SELECT * FROM `user_login` WHERE `ip` = '$ip' ORDER BY `modified` DESC LIMIT 1;");
    if(count($login)){
        return $login[0];
    }
    return NULL;
}
function GetLoginUserByToken($token){
    $login = clsDB::$db_g->select("SELECT * FROM `user_login` WHERE `token` = '$token' ORDER BY `modified` DESC LIMIT 1;");
    if(count($login)){
        return $login[0];
    }
    return NULL;
}
function CreateAnonLoginSession($ip){
    $id = clsDB::$db_g->safe_insert("user_login",[
        "user_id" => 0,
        "ip" => $ip,
        "token" => ""
    ]);
    return GetLoginUserById($id);
}
function LoginAnonUser($user_id,$login_id,$token){
    clsDB::$db_g->safe_update("user_login",['user_id'=>$user_id,"token"=>$token],['id'=>$login_id]);
    return GetLoginUserById($login_id);
}
function LogoutUserSession($id){
    clsDB::$db_g->safe_update("user_login",["token"=>""],['id'=>$id]);
    return GetLoginUserById($id);
}
function CreateServerUser($name,$mac_address){
    $user = GetUserName($name);
    if(is_null($user)){
        $id = clsDB::$db_g->safe_insert("users",["username"=>$name,"password"=>$mac_address,"level"=>3]);
    }
    return GetUserById($id);
}
function GetServerUser($name,$mac_address){
    $user = clsDB::$db_g->select("SELECT * FROM `users` WHERE `password` = '$mac_address' LIMIT 1;");
    if(count($user)){
        return $user[0];
    }
    $user = GetUserName($name);
    if(count($user)){
        return $user;
    }
    return null;
}
?>
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ChatController;

Route::get('/', function () {
    return view('welcome');
});


Route::view('/chat', 'chat'); // Page with the chat UI
Route::post('/chatbot', [ChatController::class, 'handle']); // API to handle messages

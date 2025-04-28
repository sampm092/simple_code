<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ChatController extends Controller
{
    public function handle(Request $request)
{
    $userMessage = strtolower($request->message);

    $replies = [
        'hello' => 'Hi there! 👋',
        'hi' => 'Hello! 👋',
        'how' && 'you' => "I'm doing great, thanks for asking!",
        'bye' => 'Goodbye! 👋',
        'help' => 'How can I assist you?',
        'help' && 'with' => "I'm afraid i can't do that",
        'thanks' => 'You\'re welcome!',
    ];

    $reply = "I'm not sure how to respond to that.";

    foreach ($replies as $keyword => $response) {
        if (strpos($userMessage, $keyword) !== false) {
            $reply = $response;
            break; // stop at the first matching word
        }
    }

    return response()->json(['reply' => $reply]);
}
}

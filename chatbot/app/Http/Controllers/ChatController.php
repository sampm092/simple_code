<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ChatController extends Controller
{
    public function handle(Request $request)
    {
        $userMessage = strtolower($request->message);

        $replies = [
            [
                'type' => 'and', // <-- all keywords must exist
                'keywords' => ['how', 'you'],
                'reply' => "I'm doing great, thanks for asking!"
            ],
            [
                'type' => 'single', // <-- only one keyword needed
                'keywords' => ['how'],
                'reply' => "You asked 'how' — can you be more specific?"
            ],
            [
                'type' => 'single',
                'keywords' => ['hello'],
                'reply' => 'Hi there! 👋'
            ],
            [
                'type' => 'single',
                'keywords' => ['hi'],
                'reply' => 'Hello! 👋'
            ],
            [
                'type' => 'single',
                'keywords' => ['bye'],
                'reply' => 'Goodbye! 👋'
            ],
            [
                'type' => 'single',
                'keywords' => ['help'],
                'reply' => 'How can I assist you?'
            ],
            [
                'type' => 'single',
                'keywords' => ['thanks'],
                'reply' => "You're welcome!"
            ],
        ];
    

        $reply = "I'm not sure how to respond to that.";

        foreach ($replies as $item) {
            if ($item['type'] === 'and') {
                $foundAll = true;
                foreach ($item['keywords'] as $word) {
                    if (strpos($userMessage, $word) === false) {
                        $foundAll = false;
                        break;
                    }
                }
                if ($foundAll) {
                    $reply = $item['reply'];
                    break;
                }
            } elseif ($item['type'] === 'single') {
                foreach ($item['keywords'] as $word) {
                    if (strpos($userMessage, $word) !== false) {
                        $reply = $item['reply'];
                        break 2; // break out of both foreach loops
                    }
                }
            }
        }

        return response()->json(['reply' => $reply]);
    }

}

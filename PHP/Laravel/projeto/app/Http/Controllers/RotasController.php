<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RotasController extends Controller
{
    public function getTime(Request $request) {
        $nome = $request->input('nome');
        $email = $request->input('email');
        return view('time', compact('nome', 'email'));
    }

    public function postTime(Request $request) {
        $nome = $request->input('nome');
        $email = $request->input('email');
        return view('time', compact('nome', 'email'));
    }

    public function putTime(Request $request) {
        $nome = $request->input('nome');
        $email = $request->input('email');
        return view('time', compact('nome', 'email'));
    }

     public function deleteTime(Request $request) {
        $nome = $request->input('nome');
        echo 'O nome e o email do time %s', $nome, 'foi deletado.';
    }
}

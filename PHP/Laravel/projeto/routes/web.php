<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\RotasController;
use App\Http\Controllers\TimeController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route:: get('/time', [RotasController:: class, 'getTime']);
Route:: post('/time', [RotasController:: class, 'postTime']);
Route:: put('/time', [RotasController:: class, 'putTime']);
Route:: delete('/time', [RotasController:: class, 'deleteTime']);

//Route:: resource('/time', TimeController:: class);













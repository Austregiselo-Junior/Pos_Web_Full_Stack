<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TimeModel extends Model
{
    use HasFactory;
    protected $table = 'time';
    protected $primarykey = 'id';
    protected $fillable = ['nome','email'];
}
require 'rubygems'
require 'sinatra'
require 'sinatra/reloader'
require "./calc.rb"
require "./lib/settings.rb"

enable :logging
run Sinatra::Application
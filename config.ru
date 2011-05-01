require 'rubygems'
require 'sinatra'
require 'sinatra/reloader'
require "./calc.rb"
require "./lib/settings.rb"

enable :logging
set :environment, :production
set :port, 4567
run Sinatra::Application
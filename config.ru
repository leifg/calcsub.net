require 'rubygems'
require 'sinatra'
require 'sinatra/reloader'
require "./calc.rb"
require "./lib/settings.rb"

enable :logging
set :environment, :development
set :port, 4567
#run Sinatra::Application
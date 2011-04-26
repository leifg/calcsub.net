require 'sinatra'
require 'haml'
require 'sass'
require File.join(File.dirname(__FILE__),'lib','ip_range.rb')
require File.join(File.dirname(__FILE__),'lib','frontend_helper.rb')

@@default_address = '192.168.0.1'
@@default_prefix = 24

get '/css/style.css' do
  headers \
   'Content-Type' => 'text/css; charset=utf-8'
  sass :style
end

post '/post' do
  redirect "/#{params[:address_with_prefix]}"
end

get '/:any_string' do
  set_values(params, IpRange.new(params[:any_string]))
  haml :layout
end

get '/' do
  set_values(params,nil,true)
  haml :layout
end

get '/:address/:prefix' do
  set_values(params, IpRange.new(params[:address],params[:prefix]))
  haml :layout
end


def set_values(params, data=nil, empty=nil)
  
  if (data)
    @data = data
  else
    @data = IpRange.new(nil) unless data
  end
  @empty = empty
  @frontend_helper = FrontendHelper.new(@data)
  
  if @data.valid?
    @string_for_input = "#{@data.address}/#{@data.prefix.to_s }"
  elsif params.has_key?('any_string')
    @string_for_input = params[:any_string]
  elsif params.has_key?('address')
    @string_for_input = "#{params[:address]}/#{params[:prefix]}"
  end
end
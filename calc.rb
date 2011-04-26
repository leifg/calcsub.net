require 'sinatra'
require 'haml'
require 'sass'
require 'json'
require File.join(File.dirname(__FILE__),'lib','ip_range.rb')
require File.join(File.dirname(__FILE__),'lib','frontend_helper.rb')

get '/css/style.css' do
  headers \
   'Content-Type' => 'text/css; charset=utf-8'
  sass :style
end

post '/post' do
  redirect "/#{params[:address_with_prefix]}"
end

get '/:any_string' do
  tmp_data = IpRange.new(params[:any_string])
  if tmp_data.valid?
    redirect "/#{tmp_data.address}/#{tmp_data.prefix}"
  else
    process_data(params, IpRange.new(params[:any_string]), nil)
  end
end

get '/' do
  process_data(params,nil,true)
end

get '/:address/:prefix/json' do
  content_type :json
  data = IpRange.new(params[:address],params[:prefix])
  data.json
end

get '/:address/:prefix' do
  process_data(params, IpRange.new(params[:address],params[:prefix]))
end


def process_data(params, data=nil, empty=nil)
  if data
    @data = data
  else
    @data = IpRange.new(nil)
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
  
  haml :layout
end
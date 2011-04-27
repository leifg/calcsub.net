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

get '/public/scripts/:any_script' do
  headers \
   'Content-Type' => 'application/x-javascript; charset=utf-8'
  File.read(File.join('public', 'scripts', params[:any_script]))
end

post '/post' do
  redirect "/#{params[:address_with_prefix]}"
end

get '/:any_string/expand' do
  @data = IpRange.new(params[:any_string])
  expand_string
  @string_for_input
end

['/:any_string', '/:any_string/partial'].each do |path|
  partial = path =~ /partial$/
  
  if partial
    page = :output
  else
    page = :layout
  end
  
  get path do
    tmp_data = IpRange.new(params[:any_string])
    if tmp_data.valid?
      append_string = partial ? "/partial" : nil
      redirect "/#{tmp_data.address}/#{tmp_data.prefix}#{append_string}"
    else
      process_data(params, IpRange.new(params[:any_string]), nil, page)
    end
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

get '/:address/:prefix/partial' do
  process_data(params, IpRange.new(params[:address],params[:prefix]),nil,:output)
end

helpers do
  
  def expand_string
    if @data.valid?
      @string_for_input = "#{@data.address}/#{@data.prefix.to_s }"
    elsif params.has_key?('any_string')
      @string_for_input = params[:any_string]
    elsif params.has_key?('address')
      @string_for_input = "#{params[:address]}/#{params[:prefix]}"
    end
  end
  
  def process_data(params, data=nil, empty=nil, page=:layout)
    if data
      @data = data
    else
      @data = IpRange.new(nil)
    end
    @empty = empty
    @frontend_helper = FrontendHelper.new(@data)
    expand_string
  
    haml page, :layout => false
  end
end
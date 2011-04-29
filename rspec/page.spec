require File.dirname(__FILE__) + '/spec_helper'

describe "DualCalc" do
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  it "should respond to /" do
    get '/'
    last_response.should be_ok
  end
  
  it "should respond to any string" do
    get '/any_string'
    last_response.should be_ok
  end
  
  it "should respond to any number" do
    get '/2'
    puts "the status is: #{last_response.status}"
    last_response.status.to_i.should < 400
  end
  
  it "should respond to an ip-address without prefix" do
    get '/192.168.1.1'
    last_response.status.to_i.should < 400
  end
  
  it "should respond to valid input" do
    get '/192.168.1.20/24'
    last_response.should be_ok 
  end
  
  it "should expand an ipv4 address with prefix" do
    get '/192.168.1.20/24/expand'
    last_response.should be_ok
	expected = IpRange.new("192.168.1.20",24)
    actual = IpRange.new(last_response.body)
    actual.should == expected
  end
  
  it "should expand an ipv4 address without prefix" do
    get '/192.168.1.20/expand'
    last_response.should be_ok
	expected = IpRange.new("192.168.1.20")
    actual = IpRange.new(last_response.body)
    actual.should == expected
  end
  
  it "should expand an ipv6 address without prefix" do
    get '/ff0::/expand'
    last_response.should be_ok
	expected = IpRange.new("ff0::")
    actual = IpRange.new(last_response.body)
    actual.should == expected
  end
  
  it "should expand an ipv6 address with prefix" do
    get '/ff0::/56/expand'
    last_response.should be_ok
	expected = IpRange.new("ff0::",56)
    actual = IpRange.new(last_response.body)
    actual.should == expected
  end
  
  it "should return css correctly" do
    get '/public/css/style.css' 
    last_response.headers["Content-Type"].should == "text/css; charset=utf-8"
  end
  
  it "should respond to invalid input" do
    get '/192abssb/25' 
    last_response.should be_ok 
  end
end
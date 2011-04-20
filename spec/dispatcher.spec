require File.dirname(__FILE__) + '/spec_helper'

describe IpVersionDispatcher, "when passed IPv4 address" do

  it "should return the IP-version #{:ipv4} on local address '192.168.0.1' " do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("192.168.0.1") {|ip_address, ip_version| ip_version.should be :ipv4}
  end

end

describe IpVersionDispatcher, "when passed IPv6 address" do
  
  it "should return the IP-version #{:ipv6} on local address 'FF80:0000:0000:0000:0000:0000:0000:0001' " do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("FF80:0000:0000:0000:0000:0000:0000:0001") {|ip_address, ip_version| ip_version.should be :ipv6}
  end
  
  it "should return the IP-version #{:ipv6} on local address 'FF80::' " do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("FF80::") {|ip_address, ip_version| ip_version.should be :ipv6}
  end
  
  it "should return the IP-version #{:ipv6} on local address 'FF80::1' " do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("FF80::1") {|ip_address, ip_version| ip_version.should be :ipv6}
  end
  
  it "should return the IP-version #{:ipv6} on localhost address '::1' " do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("::1") {|ip_address, ip_version| ip_version.should be :ipv6}
  end
  
  it "should return 339617752923046005526922703901628039169 on local address 'FF80:0000:0000:0000:0000:0000:0000:0001' " do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("FF80:0000:0000:0000:0000:0000:0000:0001") {|ip_address, ip_version| ip_address.should == 339617752923046005526922703901628039169}
  end
  
  it "should return 1 on localhost address '::1' " do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("::1") {|ip_address, ip_version| ip_address.should == 1}
  end
end

describe IpVersionDispatcher, "when passed invalid input" do
  it "should return 'nil' on 'nil' input" do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch(nil) {|ip_address, ip_version| ip_version.should be nil}
  end
  
  it "should return 'nil' on empty string input" do
    dispatcher = IpVersionDispatcher.new
    dispatcher.dispatch("") {|ip_address, ip_version| ip_version.should be nil}
  end
end
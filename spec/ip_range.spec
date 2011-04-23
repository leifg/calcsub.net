require File.dirname(__FILE__) + '/spec_helper'

describe IpRange, "when receiving ipv4 address" do
  
  Local_IPv4_address1 = "192.168.0.198/24"
  Local_IPv4_address2 = "127.0.0.1/32"
  IPv4_address1 = "199.59.148.83/29"
  
  it "should return the correct net address for local ip address #{Local_IPv4_address1}" do 
    metadata = IpRange.new(Local_IPv4_address1)
    metadata.net_address.should == "192.168.0.0"
  end
  
  it "should return the correct net address for local ip address #{Local_IPv4_address2}" do 
    metadata = IpRange.new(Local_IPv4_address2)
    metadata.net_address.should == "127.0.0.1"
  end
  
  it "should return the correct net address for ip address #{IPv4_address1}" do 
    metadata = IpRange.new(IPv4_address1)
    metadata.net_address.should == "199.59.148.80"
  end
  
  it "should be valid for local ip address #{Local_IPv4_address1}" do
    metadata = IpRange.new(Local_IPv4_address1)
    metadata.valid?.should be true
  end
end

describe IpRange, "when receiving ipv6 address" do

  Local_IPv6_address1_range = "fe80:0000:0000:0000:0000:0000:0000:282f/10"
  IPv6_address_range_2 = "2002:0000:0000:0000:17a4:0000:13f5:282f/3"
  IPv6_address_range_3 = "2001:910:7600::/38"
  IPv6_address_range_4 = "2a01:e00::/26"
  
  it "should return the correct net address for local ip address #{Local_IPv6_address1_range}" do 
    metadata = IpRange.new(Local_IPv6_address1_range)
    metadata.net_address.should == "fe80:0000:0000:0000:0000:0000:0000:0000"
  end
  
  it "should return the correct net address for local ip address #{IPv6_address_range_2}" do 
    metadata = IpRange.new(IPv6_address_range_2)
    metadata.net_address.should == "2000:0000:0000:0000:0000:0000:0000:0000"
  end
  
  it "should return the correct net address for local ip address #{IPv6_address_range_3}" do 
    metadata = IpRange.new(IPv6_address_range_3)
    metadata.net_address.should == "2001:0910:7400:0000:0000:0000:0000:0000"
  end
  
  it "should return the correct net address for local ip address #{IPv6_address_range_4}" do 
    metadata = IpRange.new(IPv6_address_range_4)
    metadata.net_address.should == "2a01:0e00:0000:0000:0000:0000:0000:0000"
  end

end

describe IpRange, "when receiving invalid input" do
  
  it "should return nil on nil input" do
    metadata = IpRange.new(nil)
    metadata.net_address.should == nil
  end
  
  it "should return nil on higher prefix IPv4 input" do 
    metadata = IpRange.new("192.168.1.27/33")
    metadata.net_address.should == nil
  end
  
  it "should return nil on higher prefix IPv6 input" do 
    metadata = IpRange.new("fe80:0000:0000:0000:0000:0000:0000:282f/129")
    metadata.net_address.should == nil
  end
  
  it "should be invalid on higher prefix IPv4 input" do 
    metadata = IpRange.new("192.168.1.27/33l")
    metadata.net_address.should == nil
  end
  
  it "should be invalid on higher prefix IPv6 input" do 
    metadata = IpRange.new("fe80:0000:0000:0000:0000:0000:0000:282f/129")
    metadata.net_address.should == nil 
  end
  
  it "should be invalid on nil input" do
    metadata = IpRange.new(nil)
    metadata.valid?.should be false
  end
  
end
require File.dirname(__FILE__) + '/spec_helper'

describe IpRange, "when receiving ipv4 address" do
  
  Local_IPv4_address1 = "192.168.0.198/24"
  Local_IPv4_address2 = "127.0.0.1/32"
  IPv4_address1 = "199.59.148.83/29"
  Single_IPV4_IP_Address = "127.0.0.1"
  Local_IPv4_address1_to_format = "192.168.100.198/24"
  IPv4_address2_to_format = "72.98.11.7/31"
  IPv4_address3_to_format = "88.91.18.9/21"
  IPv4_address4_to_format = "212.18.13.13/32"
  IPv4_address5_to_format = "193.13.19.98/31"
  
  it "should return the correct net address for local ip address #{Local_IPv4_address1}" do 
    metadata = IpRange.new(Local_IPv4_address1)
    metadata.net_address.should == "192.168.0.0"
  end
  
  it "should return the correct net address for local ip address #{Local_IPv4_address2}" do 
    metadata = IpRange.new(Local_IPv4_address2)
    metadata.net_address.should == "127.0.0.1"
  end
  
  it "should return the correct broadcast address for local ip address #{Local_IPv4_address1}" do 
    metadata = IpRange.new(Local_IPv4_address1)
    metadata.broadcast_address.should == "192.168.0.255"
  end
  
  it "should return the correct net address for ip address #{IPv4_address1}" do 
    metadata = IpRange.new(IPv4_address1)
    metadata.net_address.should == "199.59.148.80"
  end
  
  it "should return the correct broadcast address for ip address #{IPv4_address1}" do 
    metadata = IpRange.new(IPv4_address1)
    metadata.broadcast_address.should == "199.59.148.87"
  end
  
  it "should be valid for local ip address #{Local_IPv4_address1}" do
    metadata = IpRange.new(Local_IPv4_address1)
    metadata.valid?.should be true
  end
  
  it "should be valid for single ip address #{Single_IPV4_IP_Address}" do
    metadata = IpRange.new(Single_IPV4_IP_Address)
    metadata.valid?.should be true
  end
  
  it "should return print out the correct IP-address for local ipv4 address #{Local_IPv4_address1_to_format}" do 
    expected_result = {:net => "192.168.100.", :mixed => nil, :host => "198"}
    IpRange.new(Local_IPv4_address1_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address2_to_format}" do 
    expected_result = {:net => "072.098.011.", :mixed => "007", :host => nil}
    IpRange.new(IPv4_address2_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address3_to_format}" do 
    expected_result = {:net => "088.091.", :mixed => "018.", :host => "009"}
    IpRange.new(IPv4_address3_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address4_to_format}" do 
    expected_result = {:net => "212.018.013.013", :mixed => nil, :host => nil}
    IpRange.new(IPv4_address4_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address5_to_format}" do 
    expected_result = {:net => "193.013.019.", :mixed => "098", :host => nil}
    IpRange.new(IPv4_address5_to_format).dotted_hash.should == expected_result
  end
end

describe IpRange, "when receiving ipv6 address" do

  Local_IPv6_address1_range = "fe80:0000:0000:0000:0000:0000:0000:282f/10"
  Local_IPv6_address2_range = "ff80::/23"
  IPv6_address_range_2 = "2002:0000:0000:0000:17a4:0000:13f5:282f/3"
  IPv6_address_range_3 = "2001:910:7600::/38"
  IPv6_address_range_4 = "2a01:e00::/26"
  Single_IPV6_IP_Address = "fe80:0000:0000:0000:0000:0226:08ff:fe01"
  
  Local_IPv6_address1_to_format = "fe80:0000:0000:0000:0202:b3ff:fe1e:8329/10"
  Local_IPv6_address2_to_format = "fe80::1234:0000:0222:b3fe:fefe:6201/128"
  Local_IPv6_address3_to_format = "fe80:4218:192:0:222:4a6b:2122:6208/124"
  Local_IPv6_address4_to_format = "fe80:9271::4a6b:18e3:17b5/127"
  Local_IPv6_address5_to_format = "ff80::1/14"
  IPv6_address1_to_format = "2002::/3"
  IPv6_address2_to_format = "2003:1985::/32"
  
  it "should return the correct net address for local ip address #{Local_IPv6_address1_range}" do 
    metadata = IpRange.new(Local_IPv6_address1_range)
    metadata.net_address.should == "fe80:0000:0000:0000:0000:0000:0000:0000"
  end
  
  it "should return the correct net address for local ip address #{Local_IPv6_address2_range}" do 
    metadata = IpRange.new(Local_IPv6_address2_range)
    metadata.net_address.should == "ff80:0000:0000:0000:0000:0000:0000:0000"
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
    metadata.valid?.should be true
    metadata.net_address.should == "2a01:0e00:0000:0000:0000:0000:0000:0000"
  end
  
  it "should return the correct broadcast address for local ip address #{IPv6_address_range_3}" do 
    metadata = IpRange.new(IPv6_address_range_3)
    metadata.broadcast_address.should == "2001:0910:77ff:ffff:ffff:ffff:ffff:ffff"
  end
  
    it "should return the correct broadcast address for local ip address #{Local_IPv6_address2_range}" do 
    metadata = IpRange.new(Local_IPv6_address2_range)
    metadata.broadcast_address.should == "ff80:01ff:ffff:ffff:ffff:ffff:ffff:ffff"
  end
  
  it "should be valid for single ip address #{Single_IPV6_IP_Address}" do
    metadata = IpRange.new(Single_IPV6_IP_Address)
    metadata.valid?.should be true
  end

  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address1_to_format}" do 
    expected_result = {:net => "fe", :mixed => "8", :host => "0:0000:0000:0000:0202:b3ff:fe1e:8329"}
    IpRange.new(Local_IPv6_address1_to_format).dotted_hash.should == expected_result
  end
 
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address2_to_format}" do 
    expected_result = {:net => "fe80:0000:1234:0000:0222:b3fe:fefe:6201", :mixed => nil, :host => nil}
    IpRange.new(Local_IPv6_address2_to_format).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address3_to_format}" do 
    expected_result = {:net => "fe80:4218:0192:0000:0222:4a6b:2122:620", :mixed => nil, :host => "8"}
    IpRange.new(Local_IPv6_address3_to_format).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address4_to_format}" do 
    expected_result = {:net => "fe80:9271:0000:0000:0000:4a6b:18e3:17b", :mixed => "5", :host => nil}
    IpRange.new(Local_IPv6_address4_to_format).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address5_to_format}" do 
    expected_result = {:net => "ff8", :mixed => "0:", :host => "0000:0000:0000:0000:0000:0000:0001"}
    IpRange.new(Local_IPv6_address5_to_format).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{IPv6_address1_to_format}" do 
    expected_result = {:net => nil, :mixed => "2", :host => "002:0000:0000:0000:0000:0000:0000:0000"}
    IpRange.new(IPv6_address1_to_format).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{IPv6_address2_to_format}" do 
    expected_result = {:net => "2003:1985:", :mixed => nil, :host => "0000:0000:0000:0000:0000:0000"}
    IpRange.new(IPv6_address2_to_format).dotted_hash.should == expected_result
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
  
  it "should be invalid on non number prefix input (constructor 1)" do
    metadata = IpRange.new("2003:0000:0000:0000:0000:0000:0000:0014","1y")
    metadata.valid?.should be false
  end
  
  it "should be invalid on non number prefix input (constructor 2)" do
    metadata = IpRange.new("2003:0000:0000:0000:0000:0000:0000:0014/1y")
    metadata.valid?.should be false
  end
  
end
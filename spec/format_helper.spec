require File.dirname(__FILE__) + '/spec_helper'

describe FrontendFormatHelper, "when receiving ipv4 address" do
  
  Local_IPv4_address1_to_format = IpRange.new("192.168.100.198/24")
  IPv4_address2_to_format = IpRange.new("72.98.11.7/31")
  IPv4_address3_to_format = IpRange.new("88.91.18.9/21")
  IPv4_address4_to_format = IpRange.new("212.18.13.13/32")
  IPv4_address5_to_format = IpRange.new("193.13.19.98/31")
    
  it "should return print out the correct IP-address for local ipv4 address #{Local_IPv4_address1_to_format}" do 
    expected_result = {:net => "192.168.100.", :mixed => nil, :host => "198"}
    FrontendFormatHelper.new(Local_IPv4_address1_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address2_to_format}" do 
    expected_result = {:net => "072.098.011.", :mixed => "007", :host => nil}
    FrontendFormatHelper.new(IPv4_address2_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address3_to_format}" do 
    expected_result = {:net => "088.091.", :mixed => "018.", :host => "009"}
    FrontendFormatHelper.new(IPv4_address3_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address4_to_format}" do 
    expected_result = {:net => "212.018.013.013", :mixed => nil, :host => nil}
    FrontendFormatHelper.new(IPv4_address4_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for ipv4 address #{IPv4_address5_to_format}" do 
    expected_result = {:net => "193.013.019.", :mixed => "098", :host => nil}
    FrontendFormatHelper.new(IPv4_address5_to_format).dotted_hash.should == expected_result
  end
end

describe FrontendFormatHelper, "when receiving ipv6 address" do
  
  Local_IPv6_address1_to_format = "fe80:0000:0000:0000:0202:b3ff:fe1e:8329/10"
  Local_IPv6_address2_to_format = "fe80::1234:0000:0222:b3fe:fefe:6201/128"
  Local_IPv6_address3_to_format = "fe80:4218:192:0:222:4a6b:2122:6208/124"
  Local_IPv6_address4_to_format = "fe80:9271::4a6b:18e3:17b5/127"
  Local_IPv6_address5_to_format = "ff80::1/14"
  IPv6_address1_to_format = "2002::/3"
  IPv6_address2_to_format = "2003:1985::/32"
    
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address1_to_format}" do 
    expected_result = {:net => "fe", :mixed => "8", :host => "0:0000:0000:0000:0202:b3ff:fe1e:8329"}
    FrontendFormatHelper.new(IpRange.new(Local_IPv6_address1_to_format)).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address2_to_format}" do 
    expected_result = {:net => "fe80:0000:1234:0000:0222:b3fe:fefe:6201", :mixed => nil, :host => nil}
    FrontendFormatHelper.new(IpRange.new(Local_IPv6_address2_to_format)).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address3_to_format}" do 
    expected_result = {:net => "fe80:4218:0192:0000:0222:4a6b:2122:620", :mixed => nil, :host => "8"}
    FrontendFormatHelper.new(IpRange.new(Local_IPv6_address3_to_format)).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address4_to_format}" do 
    expected_result = {:net => "fe80:9271:0000:0000:0000:4a6b:18e3:17b", :mixed => "5", :host => nil}
    FrontendFormatHelper.new(IpRange.new(Local_IPv6_address4_to_format)).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{Local_IPv6_address5_to_format}" do 
    expected_result = {:net => "ff8", :mixed => "0:", :host => "0000:0000:0000:0000:0000:0000:0001"}
    FrontendFormatHelper.new(IpRange.new(Local_IPv6_address5_to_format)).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{IPv6_address1_to_format}" do 
    expected_result = {:net => nil, :mixed => "2", :host => "002:0000:0000:0000:0000:0000:0000:0000"}
    FrontendFormatHelper.new(IpRange.new(IPv6_address1_to_format)).dotted_hash.should == expected_result
  end
  
  it "should print out the correct IP-address for ipv6 address #{IPv6_address2_to_format}" do 
    expected_result = {:net => "2003:1985:", :mixed => nil, :host => "0000:0000:0000:0000:0000:0000"}
    FrontendFormatHelper.new(IpRange.new(IPv6_address2_to_format)).dotted_hash.should == expected_result
  end
end